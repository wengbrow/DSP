import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
frequency = 5  # Frequency of the wave (in Hz)
duration = 1  # Duration of the wave (in seconds)
amplitude = 1  # Amplitude of the wave

# Generate the time values
sampling_rate = 10  # Number of samples per second
samples = int(sampling_rate * duration)
t = np.linspace(0, duration, samples, endpoint=False)

# Generate the sound wave
wave = amplitude * np.sin(2 * np.pi * frequency * t)

# Plot the sound wave
plt.plot(t, wave)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sound Wave Graph')
plt.grid(True)
plt.show()