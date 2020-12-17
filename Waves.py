import numpy as np
import pyaudio
import time


class Sine:

    def __init__(self, duration, sampleRate):
        self.sampleRate = sampleRate
        self.waveTable = [np.float] * int(sampleRate * duration)       # changing for np datatype
        self.lastPhase = np.pi * 2
        self.phaseInc = 0
        self.phase = 0
        self.fullWave = np.pi * 2
        self.setFrequency(0)

    def setFrequency(self, frequency):
        self.phaseInc = np.float32((self.fullWave * frequency) / self.sampleRate)  # changing for np datatype

    def dynBuffer(self):

        for i in range(len(self.waveTable)):
            self.phase += self.phaseInc
            if self.phase > self.fullWave:
                self.phase = self.phase - self.fullWave

            self.waveTable[i] = self.phase

        self.waveTable = np.sin(self.waveTable)
        self.waveTable /= self.fullWave / 4.
        _waveTable = np.array(self.waveTable).astype(np.float32).tobytes()
        print(self.lastPhase)

        return _waveTable

