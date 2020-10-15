from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import functions as fn

fs=80000
f=8000
fnorm=f/fs #Normalized Frequency = 0.1
time_duration=0.001
n=np.arange(-time_duration*fs,time_duration*fs,0.25).astype(np.float32)
Amp=1
t=n/fs
bitsize=8

#Generating Full Range Triangle Signal
triangle=fn.Signal_gen(fs,f,Amp,time_duration,'triangle')
#Generating Triangle Signal 25dB Below Full Range
db_triangle= fn.db_range(triangle, 25)
#Difference in signals
diff_signal=triangle - db_triangle

print("Difference Between Triangular signals is",diff_signal)


#Playing the Generated Full Range Signal
print('Playing Triangular Function with Full Range')
fn.signal_play(triangle, fs, 1)
#Playing the Signal 25dB Below Full Range
print('Playing Triangular Function with 25dB below Full Range')
fn.signal_play(db_triangle, fs, 1)
SNR=fn.SNR(triangle,bitsize,"midrise")
print("Midrise has SNR for Triangular wave", SNR,"dB")
SNR=fn.SNR(triangle,bitsize,"midtread")
print("Midtread has SNR for Triangular wave", SNR,"dB")
figure,(t1,t2) = plt.subplots(2)
t1.plot(t,triangle)
t1.set_ylabel('Amplitude(A)')
t1.set_title('Full Range Signal Plot of Triangular Wave')
t2.plot(t, db_triangle)
t2.set_ylabel('Amplitude(A)')
t2.set_title('25dB Below Full Range Signal Plot of Triangular Wave')
plt.show()


sine=fn.Signal_gen(fs,f,Amp,time_duration,'sine')
#Generating Sine Signal 25dB Below Full Range
db_sine= fn.db_range(sine, 25)
#Difference in signals
diff_signal=sine - db_sine

print("Difference Between Sine signals is",diff_signal)


#Playing the Generated Full Range Signal
print('Playing Sine Wave with Full Range')
fn.signal_play(sine, fs, 1)
#Playing the Signal 25dB Below Full Range
print('Playing Sine Wave with 25dB below Full Range')
fn.signal_play(db_sine, fs, 1)
#Determining SNR of Signal with both Midtread and Midrise
SNR=fn.SNR(sine,bitsize,"midrise")
print("Midrise has SNR for Sine wave", SNR,"dB")
SNR=fn.SNR(sine,bitsize,"midtread")
print("Midtread has SNR for Sine wave", SNR,"dB")

#Plotting Both signal in a Single Figure
figure,(s1,s2) = plt.subplots(2)
#Plotting Full Range Sine Signal
s1.plot(t,sine)
s1.set_ylabel('Amplitude(A)') #Y-axis
s1.set_title('Full Range Plot of Sine Wave')
#Ploting the Signal 25dB Below Full Range
s2.plot(t, db_sine)
s2.set_ylabel('Amplitude(A)') #Y-axis
s2.set_title('25dB Below Plot of Sine Wave')
plt.show()

Fs, Signal = wavfile.read('Track48.wav','r')
#Estimating the time of the Track48.wav file
Signal1 = Signal[:, 0]
Sig_Duration= len(Signal)/Fs
Time=np.linspace(0, Sig_Duration, len(Signal))
#Determining the Number of channels in WavFile
channels= fn.channels('Track48.wav')
print("Playing Full Range Audio")
fn.signal_play(Signal,Fs,channels)
#New Signal 25dB below full range
db_signal=fn.db_range(Signal,25)
db_Signal1 = db_signal[:, 0]
print("Playing 25dB Below Full Range Audio")
fn.signal_play(db_signal,Fs,channels)
#Difference in signals
diff_signal=Signal1 - db_Signal1

print("Difference Between the Audio signals is",diff_signal)

figure,(w1,w2) = plt.subplots(2)
#Plotting Full Range Audio
w1.plot(Time,Signal1)
w1.set_ylabel('Amplitude(A)') #Y-axis
w1.set_xlabel('Time(T)                                                                                                                                  ') #X-axis
w1.set_title('Full Range Signal Plot of Audio')
#Ploting the Signal 25dB Below Full Range
w2.plot(Time, db_Signal1)
w2.set_ylabel('Amplitude(A)') #Y-axis
w2.set_xlabel('Time(T)                                                                                                                                  ') #X-axis
w2.set_title('25dB Below Full Range Signal Plot of Audio')
plt.show()




