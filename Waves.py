import numpy as np
import pyaudio
import time


class Sine:

    def __init__(self, duration, sampleRate):
        self.duration = duration
        self.sampleRate = sampleRate
        self.phase = 0
        self.bufferSize = int(sampleRate * duration)
        self.waveTable = [np.float] * self.bufferSize       # changing for np datatype
        self.lastPhase = np.pi * 2

    def getBuffer(self, frequency):
        phaseInc = ((2 * np.pi * np.arange(self.bufferSize) * frequency / self.sampleRate) + self.phase).astype(np.float32)
        self.phase = phaseInc[len(phaseInc) - 1]
        buffer = np.sin(phaseInc)
        print(self.phase)
        return buffer

    def dynBuffer(self, frequency):
        # frequency = 200
        phaseInc = np.float32((np.pi * 2.) * frequency * (1. / self.sampleRate))    # changing for np datatype
        phase = 0.0

        for i in range(len(self.waveTable)):
            phase += phaseInc

            if phase > (np.pi * 2.):
                phase = 0.0

            self.waveTable[i] = phase + self.lastPhase

        #self.lastPhase = self.waveTable[len(self.waveTable) - 1]
        #self.lastPhase = self.waveTable[0]
        self.waveTable = np.sin(self.waveTable)
        _waveTable = np.array(self.waveTable).astype(np.float32).tobytes()
        print(self.lastPhase, frequency)

        return _waveTable

