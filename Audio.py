import numpy as np
import pyaudio
import time
from Waves import Sine
p = pyaudio.PyAudio()


"""
Keep 'Get sine wave at buffersize (0.03seconds == 30millis == 30fps),
call this every buffer to keep sine continuety


"""


class Audio:

    def __init__(self):
        self.volume = 0.5     # range [0.0, 1.0]
        self.fs = 44100       # sampling rate, Hz, must be integer
        self.bufferSize = 0.3   # in seconds, may be float       0.03 == 30ms delay
        self.stream = p.open(format=pyaudio.paFloat32,
                             channels=1,
                             rate=self.fs,
                             frames_per_buffer = int(self.fs * self.bufferSize),
                             stream_callback = self.callback,
                             output=True)

        self.sineWave = Sine(self.bufferSize, self.fs)
        pass

    def callback(self, in_data, frame_count, time_info, status):
        buffer = self.updateSoundStream()
        return (buffer, pyaudio.paContinue)

    def updateSoundStream(self):
        buffer = self.volume * self.sineWave.getBuffer(500)
        return buffer

        # generate samples, note conversion to float32 array

    def stopStream(self):
        stream.stop_stream()
        stream.close()
        p.terminate()
    # for paFloat32 sample values must be in range [-1.0, 1.0]
