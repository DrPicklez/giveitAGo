import numpy as np
import pyaudio
import time


class Sine:

    def __init__(self, duration, fs):
        self.duration = duration
        self.fs = fs

    def getBuffer(self, frequency):
        buffer = (np.sin(2 * np.pi * np.arange(self.fs * self.duration) * frequency / self.fs)).astype(np.float32)
        return buffer

