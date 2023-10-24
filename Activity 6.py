import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

class Noise:
    def __init__(self, amp):
        self.amp = amp

    def evaluate(self, time):
        raise NotImplementedError("Subclass must implement evaluate")

class UncorrelatedPoissonNoise(Noise):
    def __init__(self, amp, seed=42):
        super().__init__(amp)
        self.seed = seed
        np.random.seed(self.seed)

    def evaluate(self, time):
        poisson_noise = np.random.poisson(lam=self.amp, size=time.shape)
        return poisson_noise

def generate_up_noise(duration, amp, sample_rate):
    time = np.arange(0, duration, 1/sample_rate)
    up_noise = UncorrelatedPoissonNoise(amp)
    return up_noise.evaluate(time)

def plot_power_spectrum(signal, sample_rate):
    f = fft(signal)
    f = f[0:int(f.shape[0]/2)]
    f = np.abs(f)
    freq = np.arange(0, int(f.shape[0])*1.0/f.shape[0]*sample_rate/2, 1.0/f.shape[0]*sample_rate/2)
    plt.figure()
    plt.plot(freq, f, color='k')
    plt.title('Power Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power')
    plt.show()

def listen_to_up_noise(up_noise):
    import sounddevice as sd
    sd.play(up_noise, blocking=True)

if __name__ == "__main__":
    amp = 0.001
    duration = 1 # second
    sample_rate = 10000 # Hz