# Dopplersignal
In dieser Hausaufgabe wurde die Anregungswelle des Wandlers sowie verschiedene Dopplersignale angezeigt.
Zuerst wurde den Haupt-Code als eine Python-Datei geschrieben unter der Name "Hausaufgabe_Doppler.py" und von dieser Datei wurde alle module in eine andere Python-Datei nämlich "Importing_Hausaufgabe_Doppler.py" importiert.

Teil 1 "Hausaufgabe_Doppler.py"

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

Teil 2 "Importing_Hausaufgabe_Doppler.py"
from Hausaufgabe_Herr_Schie import *

'''sig = uSig'''
Anregungswelle (uSig, T, 'Anregungswelle des Wandlers')


'''sig = zss'''
Anregungswelle (zss, T, 'zurückkommende signal von stationärer quelle')

'''sig = bs'''
Anregungswelle (bs, T, 'dopplersignal: zurückkommende signal von beweglicher quelle')


'''sig = mix'''
Anregungswelle (mix, T, 'Gemischte Signal von Detektor', mitOrig='yes')




## Plot der Anregungswelle
![](Bilder%20Dopplersignale/Anregungswelle%20des%20Wandlers.png)



## Plot des reinen Dopplersignals
![](Bilder%20Dopplersignale/zurückkommende%20signal%20von%20beweglicher%20quelle.png)



## Plot des zurückkommenden gemischten Dopplersignals
![](Bilder%20Dopplersignale/zurückkommende%20signal%20von%20stationärer%20quelle.png)



## Plot des Dopplersignals nach dem Mixer
![](Bilder%20Dopplersignale/MixedSignal%20vom%20Detektor.png)
