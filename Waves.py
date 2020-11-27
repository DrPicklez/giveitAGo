import numpy as np
import pyaudio
import time


class Sine:

    def __init__(self, duration, sampleRate):
        self.duration = duration
        self.sampleRate = sampleRate

    def getBuffer(self, frequency):
        buffer = (np.sin(2 * np.pi * np.arange(self.sampleRate * self.duration) * frequency / self.sampleRate)).astype(np.float32)
        return buffer

