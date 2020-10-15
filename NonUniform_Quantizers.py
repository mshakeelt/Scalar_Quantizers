from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import functions as fn
from scipy.io import wavfile
import pyaudio
import scipy.io as wav


filename= 'Track48.wav'
bitsize=8
Fs, Signal = wavfile.read(filename,'r')
#Estimating the time of the wav file
Sig_Duration= len(Signal)/Fs 
Time=np.linspace(0, Sig_Duration, len(Signal))
#Determining the Number of channels in WavFile
channels= fn.channels(filename)
print("Playing the signal")
fn.signal_play(Signal,Fs,channels)
#Defining the Reconstructed signal
signal_reconstruct3=fn.mid_tread(Signal,bitsize)
#Quantization Error
Q_error=Signal[0,0]- signal_reconstruct[0,0]
print("Quantization error for Mid Tread quantizer is", Q_error)
#Playing the Reconstructed signal
print("Playing the reconstructed signal")
fn.signal_play(signal_reconstruct,Fs,channels)
#Determining SNR of the signal
SNR=fn.SNR(Signal,bitsize,"midtread")
print("SNR of Track48.wav with midtread is", SNR,"dB")

#Plotting
fig,(a1,a2) = plt.subplots(2)
a1.plot(Time, Signal[:,0], 'r', label='Original Signal' )
a1.plot(Time,signal_reconstruct[:,0], 'g:', label='Reconstructed Signal (MidTread)')
a2.plot(Time,Signal[:,1], 'b',label='Original Signal')
a2.plot( Time, signal_reconstruct[:,1], 'r:', label='Reconstructed Signal (MidTread)')
a1.set_title('Channel 1')
a1.set_ylabel('Amplitude')
a1.set_xlabel('Time -->')
a2.set_title('Channel 2')
a2.set_ylabel('Amplitude')
a2.set_xlabel('Time -->')
leg=a1.legend()
leg=a2.legend()

plt.show()


#Reconstructing the Signal Using Mid Rise
signal_reconstruct=fn.mid_rise(Signal,bitsize)
print("Playing the reconstructed signal")
#Playing the Reconstructed Signal
fn.signal_play(signal_reconstruct,Fs,channels)
#Quantization Error
Q_error = Signal[0,0]-signal_reconstruct[0,0]
print("Quantization error for Mid rise quantizer is", Q_error)
#Determining the SNR of the Signal
SNR=fn.SNR(Signal,bitsize,"midrise")
print("SNR of Track48.wav with midrise is", SNR,"dB")
#Plotting
fig,(a1,a2) = plt.subplots(2)
a1.plot(Time, Signal[:,0], 'r', label='Original Signal' )
a1.plot(Time,signal_reconstruct[:,0], 'g:', label='Reconstructed Signal (MidRise)')
a2.plot(Time,Signal[:,1], 'b',label='Original Signal')
a2.plot( Time, signal_reconstruct[:,1], 'r:', label='Reconstructed Signal (MidRise)')
a1.set_title('Channel 1')
a1.set_ylabel('Amplitude')
a1.set_xlabel('Time -->')
a2.set_title('Channel 2')
a2.set_ylabel('Amplitude')
a2.set_xlabel('Time -->')
leg=a1.legend()
leg=a2.legend()

plt.show()


#Defining the Reconstructed signal with u_Law Mid Tread
signal_reconstruct4=fn.u_Law(Signal,bitsize,'midtread')
print("Playing the ulaw Midtread reconstructed signal")
fn.signal_play(signal_reconstruct1,Fs,channels)
#Quantization Error with ulaw Midtread
Q_error1= Signal[0,0] - signal_reconstruct1[0,0]
print("Quantization error for u_Law Midtread quantizer is", Q_error1)

#Defining the Reconstructed signal with u_Law Mid Rise
signal_reconstruct2=fn.u_Law(Signal,bitsize,'midrise')
print("Playing the ulaw Midrise reconstructed signal")
fn.signal_play(signal_reconstruct2,Fs,channels)
#Quantization Error with ulaw Midrise
Q_error2= Signal[0,0] - signal_reconstruct2[0,0]
print("Quantization error for u_Law Midrise quantizer is", Q_error2)

#SNR with ulaw Midtread
SNR=fn.SNR(Signal,bitsize,'ulaw2')
print('SNR of Signal with uLaw Midtread is',SNR,'dB')
SNR=fn.SNR(Signal,bitsize,'ulaw1')
print('SNR of Signal with uLaw Midrise is',SNR,'dB')
#Plotting
fig,(a1,a2) = plt.subplots(2)
a1.plot(Time, signal_reconstruct3[:,0], 'r', label='Reconstructed Signal (MidTread)' )
a1.plot(Time,signal_reconstruct4[:,0], 'g:', label='Reconstructed Signal (ulaw MidTread)')
a2.plot(Time,signal_reconstruct3[:,1], 'b',label='Reconstructed Signal (MidTread)')
a2.plot( Time, signal_reconstruct4[:,1], 'r:', label='Reconstructed Signal (u_Law Midtread)')
a1.set_title('Channel 1')
a1.set_ylabel('Amplitude')
a1.set_xlabel('Time -->')
a2.set_title('Channel 2')
a2.set_ylabel('Amplitude')
a2.set_xlabel('Time -->')
leg=a1.legend()
leg=a2.legend()

plt.show()
