import numpy as np
import sounddevice as sd
from scipy.io import wavfile
from scipy.fftpack import fft
import time
from matplotlib import pyplot as plt


SAMPLE_FREQ = 44100  # Sampling frequency of the recording
SAMPLE_DUR = 2  # Duration of the recording


def record(output_name='example1.wav'):
    print("Grab your guitar!")
    time.sleep(1)  # Gives you a second to grab your guitar

    my_recording = sd.rec(SAMPLE_DUR * SAMPLE_FREQ, samplerate=SAMPLE_FREQ, channels=1, dtype='float64')
    print("Recording audio")
    sd.wait()

    sd.play(my_recording, SAMPLE_FREQ)
    print("Playing audio")
    sd.wait()

    wavfile.write(f'{output_name}', SAMPLE_FREQ, my_recording)


def plot(path: str = 'example1.wav'):
    rate, data = wavfile.read(path)
    sample_duration = len(data) / rate
    timeX = np.arange(0, sample_duration, 1 / rate)

    # Plot record
    plt.plot(timeX, data)
    plt.ylabel("x(k)")
    plt.xlabel("time[s]")
    plt.show()

    # Plot dft
    timeX = np.arange(0, rate / 2, 1 / sample_duration)
    abs_frequency_spectrum = abs(fft(data))
    plt.plot(timeX, abs_frequency_spectrum[:len(abs_frequency_spectrum) // 2])
    plt.ylabel("|X(n)|")
    plt.xlabel("Frequency[Hz]")
    plt.show()
