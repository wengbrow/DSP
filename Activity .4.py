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