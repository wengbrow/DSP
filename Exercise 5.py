import numpy as np
import matplotlib.pyplot as plt

def spectrum(t, fs):
    w = 2 * np.pi * fs
    x = np.cos(w * t)
    spectrum = np.fft.fft(x)
    spectrum = np.abs(spectrum) / len(spectrum)
    spectrum = spectrum[range(len(spectrum) // 2)]
    return spectrum

def sawtooth_chirp(t, f0, df):
    return np.mod(f0 + df * t, 1)

t = np.linspace(0, 1, 1000)
f0 = 440
df = 50

freqs = np.fft.fftfreq(len(t), d=1/len(t))
freqs = freqs[range(len(freqs) // 2)]

chirp = sawtooth_chirp(t, f0, df)
chirp_spectrum = spectrum(chirp, fs=1)

plt.plot(freqs, chirp_spectrum)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Spectrum of Sawtooth Chirp')
plt.show()
