import numpy as np
import matplotlib.pyplot as plt


E = 1
N = 10000
ft = 1
fd= 0.9
T = 0.006
p1 = 0.5
p2 = 0.5

t = np.linspace(0, T*N, N)
uSig = E*np.sin(2*np.pi*ft*t)
zss = E*p1*np.sin(2*np.pi*ft*t)
zsb = E*p2*np.sin(2*np.pi*fd*t)
bs = zss + zsb
mix = bs*np.sin(2*np.pi*ft*t)

def Anregungswelle(sig,T, title='',mitOrig='no'):
    fourier=np.fft.rfft(sig)
    ampli=np.abs(fourier)
#    anzahlFrequenzen=len(ampli)
#    print(anzahlFrequenzen)
    xWerteFreq=np.linspace(0, 1/(2*T), N//2 +1)
    
    if mitOrig == 'yes':
        plt.figure()
        plt.subplot(2,1,1)
        plt.title(title)
        plt.plot(t,sig)
        plt.subplot(2,1,2)
        plt.plot(xWerteFreq,ampli)
        plt.show() 
        
    else:
        plt.figure()
        plt.title(title)
        plt.plot(t,sig)
        plt.show() 
