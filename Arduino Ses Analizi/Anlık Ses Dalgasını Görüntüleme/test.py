import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
import time

#%matplotlib tk

CHUNK = 1024 * 4 # Audio samples per frame display
FORMAT = pyaudio.paInt16 # bytes per sample
CHANNELS = 1  # Mikrofon kullandığımızdan tek kanal olacak
RATE = 44100 # Samples per second

p = pyaudio.PyAudio()

chosen_device_index = -1
stream = p.open(format=FORMAT,
 channels=CHANNELS,
 rate=RATE,
 input_device_index=chosen_device_index,
 input=True,
 output=True,
 frames_per_buffer=CHUNK
 )
#plt.ion()
data = stream.read(CHUNK) # byte olarak basıyor
#print(len(data)) # CHUNK ın 2 katı 4096 *2

#data_int = struct.unpack(str(2 * CHUNK)+'B', data)
#print(data)
#print(data_int)
fig, ax = plt.subplots()
x = np.arange(0,2 * CHUNK,2) # 2 ise stepsize
#line, = ax.plot(x,np.random.rand(CHUNK))# Önce line çekiyoruz update olacağı için random data attık
#data_int = struct.unpack(str(CHUNK) + 'h', data)
data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), dtype='b')[::2] +127
line, = ax.plot(x, data_int)
#ax.set_ylim(0,255)
ax.set_xlim(0,2*CHUNK)
ax.set_ylim(-5000,5000)
#ax.set_ylim([-2 ** 15, (2 ** 15) - 1])

while True:
    data = struct.unpack(str(CHUNK) + 'h', stream.read(CHUNK))
    #data = stream.read(CHUNK)  # byte olarak basıyor
    #data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), dtype='b')[::2] + 128 # 2 YE Böldük [::2] # dtype b integer 0-255 - [::2] tüm diğer noktaları al sonuç olarak örnekler 0
    line.set_ydata(data)
    fig.canvas.draw()
    fig.canvas.flush_events()
    fig.show()




#ax.plot(data_int,'-')
#plt.show() # Tek CHUNKIN data görüntüsü





