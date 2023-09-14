import os

if not os.path.exists('thinkdsp.py'):
    !wget https://github.com/AllenDowney/ThinkDSP/raw/master/code/thinkdsp.py 
    from thinkdsp import TriangleSignal
from thinkdsp import decorate
signal = SawtoothSignal(500)
wave = signal.make_wave(duration=1, framerate=20000)
segment = wave.segment(duration=0.005)
segment.plot()
decorate(xlabel='Time (s)')
wave = signal.make_wave(duration=0.5, framerate=20000)
wave.apodize()
wave.make_audio()
spectrum = wave.make_spectrum()
spectrum.plot()
decorate(xlabel='Frequency (Hz)')


import numpy as np
from thinkdsp import Chirp, normalize, unbias, PI2, decorate

class SawtoothChirp(Chirp):
    """Represents a sawtooth waveform with a frequency that increases linearly."""

    def evaluate(self, ts):
        """Evaluates the signal at the given times.

        ts: float array of times
        """
        freqs = np.linspace(self.start, self.end, len(ts))
        dts = np.diff(ts, prepend=0)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        phases = np.mod(phases, PI2)
        ys = normalize(unbias(phases), self.amp)
        return ys

# Create a SawtoothChirp signal from 220 Hz to 880 Hz
signal = SawtoothChirp(start=220, end=880)

# Generate the wave and plot the waveform
wave = signal.make_wave(duration=5, framerate=44100)
wave.plot()
decorate(xlabel='Time (s)')

# Plot the spectrogram
spectrogram = wave.make_spectrogram(1024)
spectrogram.plot()
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')