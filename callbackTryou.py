# Generate a 250 Hz tone in chunks amounting to 100 chunks per second,
# using a non-blocking method.
#
# How does one fit a 250 Hz wave into 100 Hz packets?
# Slice up a sine wave into segments of two-and-a-half waves apiece:
#
#               |              |              |              |
#  _     _     _|    _     _   | _     _     _|    _     _   |
# / \   / \   / \   / \   / \   / \   / \   / \   / \   / \
#    \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/
#               |              |              |              |
#  <----X1----> | <----X2----> | <----X1----> | <----X2----> |
#
# Play back each segment in alternating fashion.
# This simulates continuous audio where zero crossings do not necessarily
# occur at the edge of a chunk.

import numpy as np
import pyaudio
import time
import queue

# based on examples from https://people.csail.mit.edu/hubert/pyaudio/docs/
def callback(in_data, frame_count, time_info, status):
    Y = qu.get()
    waveData = Y.tobytes()
    return (waveData, pyaudio.paContinue)

qu = queue.Queue(maxsize = 1)           # 1 complete buffer (of length 441)
Y = np.zeros((441), dtype = np.int16)   # initialize audio array Y
p = pyaudio.PyAudio()
stream = p.open(format = 8,             # 8 is code for int16 format
           channels = 1,
           rate = 44100,
           frames_per_buffer = 441,
           stream_callback = callback,
           output = True)

stream.start_stream()

X1 = np.linspace(0, 5 * np.pi, num = 441, endpoint = False)
Y1 = (5000 * np.sin(X1)).astype(np.int16) # Generate two-and-a-half waves

X2 = np.linspace(5 * np.pi, 10 * np.pi, num = 441, endpoint = False)
Y2 = (5000 * np.sin(X2)).astype(np.int16) # The "other" two-and-a-half waves

# Play the two wave segments one after the other
# Result should be a clean 250 Hz tone
while True:
    qu.put(Y1)                          # First set of waves
    time.sleep(0.0015)                  # This 1.5 millisecond delay
                                        #   simulates other stuff happening
                                        #   within the While loop.
    qu.put(Y2)                              # Second set of waves
    time.sleep(0.0015)                  # More miscellaneous delays
