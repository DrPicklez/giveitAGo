import numpy as np
import pyaudio
import time


class Sine:

    def __init__(self, duration, sampleRate):
        self.sampleRate = sampleRate
        self.waveTable = [np.float] * int(sampleRate * duration)       # changing for np datatype
        self.lastPhase = np.pi * 2
        self.setFrequency(0)
        self.phaseInc = 0
        self.phase = 0

    def setFrequency(self, frequency):
        self.phaseInc = np.float32((np.pi * 2.) * frequency * (1. / self.sampleRate))  # changing for np datatype

    def dynBuffer(self):

        for i in range(len(self.waveTable)):
            self.phase += self.phaseInc
            if self.phase > (np.pi * 2.):
                self.phase = (self.phase - (np.pi * 2))

            self.waveTable[i] = self.phase + self.lastPhase

        self.waveTable = np.sin(self.waveTable)
        _waveTable = np.array(self.waveTable).astype(np.float32).tobytes()
        print(self.lastPhase)

        return _waveTable

