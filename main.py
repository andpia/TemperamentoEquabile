
import numpy as np
import sounddevice as sd

def play_pure_tone(duration, frequency, volume=0.3, sample_rate=44100):
    t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
    samples = volume * np.sin(2 * np.pi * frequency * t)
    sd.play(samples, sample_rate)
    sd.wait()

# Parametri per generare un tono puro
duration = 5  # Durata in secondi
frequency = 440  # Frequenza in Hertz
volume = 1.0  # Volume (da 0 a 1)
sample_rate = 44100  # Frequenza di campionamento in Hertz

# Riproduce il tono puro
play_pure_tone(duration, frequency, volume, sample_rate)