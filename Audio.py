import numpy as np
import pyaudio
import time
from Waves import Sine
p = pyaudio.PyAudio()


"""
Keep 'Get sine wave at bufferSize (0.03seconds == 30millis == ~30fps (CameraRate)),
call this every buffer to keep sine continuity
"""


class Audio:

    def __init__(self):
        self.volume = 0.25     # range [0.0, 1.0]
        self.sampleRate = 44100       # sampling rate, Hz, must be integer
        self.bufferSize = 0.005   # in seconds, may be float       0.03 == 30ms delay
        self.bufferSizeinSamps = int(self.sampleRate * self.bufferSize)
        self.buffer = np.empty([self.bufferSizeinSamps]).astype(np.float32).tobytes()
        self.stream = p.open(format=pyaudio.paFloat32,
                             channels=1,
                             rate=self.sampleRate,
                             frames_per_buffer = self.bufferSizeinSamps,
                             stream_callback = self.callback,
                             output=True)
        self.sineWave = Sine(self.bufferSize, self.sampleRate)
        pass

    def playSine(self, frequency):
        self.buffer = self.sineWave.dynBuffer(frequency)
        pass

    def callback(self, in_data, frame_count, time_info, status):
        # Sends buffer to sound card
        return (self.buffer, pyaudio.paContinue)

        # generate samples, note conversion to float32 array

    def stopStream(self):
        stream.stop_stream()
        stream.close()
        p.terminate()
        pass
    # for paFloat32 sample values must be in range [-1.0, 1.0]
