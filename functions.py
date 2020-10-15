#Functions

from scipy import signal, stats, integrate
import matplotlib.pyplot as plt
import numpy as np
import pyaudio
import struct
import wave

def db_range(input_signal, dB): #To Play with new SNR
    c = 10.0**(dB/20.0)
    return input_signal/c

def signal_play(data, fs, channels):    #To play the audio
    p = pyaudio.PyAudio() #Initializing PYAudio
    if data.dtype == np.int8: #For 8 bit input
            #Opening the media stream
        stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=fs,
                    output=True)
        data = data.astype(np.int8).tostring()

    #Playing the media stream 
        stream.write(data)
        stream.close()
    else:
        stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=fs,
                    output=True)

        data = data.astype(np.int16).tostring()
    
        stream.write(data)
        stream.close() #Closing the media stream
   

def channels(filepath):
    data=wave.open(filepath) #Opeining WaveFile and acquiring data
    channels=wave.Wave_read.getnchannels(data) #Getting Channels
    return channels



def mid_tread(Signal_Data, bit_size):
    step = (float(np.amax(Signal_Data))-float(np.amin(Signal_Data))) / pow (2,bit_size)
    
    #In Mid Tread Quantizer index = round of Signal_Data/step
    index = np.round(Signal_Data/step)
    
    #Reconstruction of Signal
    #reconstruct = np.array(Signal_Data.shape)

    reconstruct=index*step
    #reconstruct= reconstruct.astype(np.int8)    
    return reconstruct
    
"""
Defining a function for Mid Rise Quantizer which takes input of Signal_Data
and Num of bit_size 
"""


def mid_rise(Signal_Data, bit_size):
  
    #step delta = Amax-Amin/2^N
    step = (float(np.amax(Signal_Data))-float(np.amin(Signal_Data))) / pow (2,bit_size)
    
    #In Mid Rise Quantizer index = floor of Signal_Data/step
    index = np.floor(Signal_Data/step)

    #Reconstruction of Signal
    #reconstruct = np.array(Signal_Data.shape)
    
    reconstruct=index * step + step/2
    #reconstruct= reconstruct.astype(np.int8)
    return reconstruct

def u_Law(Signal_Data, bit_size, quantizer):
    S_Max  =  float(np.amax(Signal_Data))
#    S_Min  = float(np.amin(Signal_Data))
    u = 255.0

    #u-Law Compression Expression
    Signal_y=np.sign(Signal_Data)*(np.log(1+ u* np.abs(Signal_Data/S_Max)))/np.log(1 + u)
    #Quantizer Selection

    if quantizer == 'midtread':
        Signal_yrek = mid_tread(Signal_y, bit_size)
        print("Signal has been uniformly quantized using Mid Tread Quantizer")
    elif quantizer == 'midrise':
        Signal_yrek = mid_rise(Signal_y, bit_size)
        print("Signal has been uniformly quantized using Mid Rise Quantizer")
    elif quantizer == 0:
        Signal_yrek=Signal_y
        print("Signal has not been uniformly quantized (Y=Yrek)")
            

   #u-law Expansion Expression
    reconstruct = np.sign(Signal_yrek)*(256**(np.abs(Signal_yrek))-1)*S_Max/u
    

    #reconstruct= reconstruct.astype(np.int8)
    return reconstruct
        

    

def SNR(Signal_Data, bit_size, quantizer):

#Checking Quantizer
    Eng_Signal=0.0
    Eng_Error=0.0
    if quantizer == 'midtread':
        Signal_Quantization = mid_tread(Signal_Data, bit_size)
    elif quantizer == "midrise":
        Signal_Quantization = mid_rise(Signal_Data, bit_size)
    elif quantizer == "ulaw2":
        Signal_Quantization=u_Law(Signal_Data, bit_size,'midtread')
    elif quantizer == "ulaw1":
        Signal_Quantization=u_Law(Signal_Data, bit_size,'midrise')   
#Error Signal    
    Error_Signal= Signal_Data - Signal_Quantization
#Energy in Original Signal
    Eng_Signal = np.sum(np.square(Signal_Data))
#Energy in Error Signal
    Eng_Error = np.sum(np.square(Error_Signal))
#SNR = 10* log10(Signal Energy/Quantization Error Energy
    SNR= 10 * np.log10(Eng_Signal/Eng_Error)
    return SNR

def Signal_gen(SamplingFreq, Freq, Amplitude, duration, wave):
    n=np.arange(-duration*SamplingFreq,duration*SamplingFreq,0.25).astype(np.float32)
#if phase in sawthooth is 1 or 0 its tilted right if or tilted left
#phase value 0.5 keeps it centered to give us trianglular waveform  

    if wave == 'triangle':
        return Amplitude * signal.sawtooth(2 * np.pi * (Freq/SamplingFreq) * n, 0.5)
    elif wave == 'sine':
        return Amplitude * np.sin(2 * np.pi * (Freq/SamplingFreq) * n).astype(np.float32)
