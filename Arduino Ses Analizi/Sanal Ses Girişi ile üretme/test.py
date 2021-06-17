import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
import math
import threading
import time
import serial
import random

arduinoSerialData = serial.Serial('com3', 9600)


def sesUretme(deger):
    print(deger," Hz lik dalga üretildi.")
    PyAudio = pyaudio.PyAudio  # initialize pyaudio

    # See https://en.wikipedia.org/wiki/Bit_rate#Audio
    BITRATE = 16000  # number of frames per second/frameset.

    FREQUENCY = deger  # Hz, waves per second, 261.63=C4-note.
    LENGTH = 30  # seconds to play sound

    if FREQUENCY > BITRATE:
        BITRATE = FREQUENCY + 100

    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    RESTFRAMES = NUMBEROFFRAMES % BITRATE
    WAVEDATA = ''

    # generating wawes
    for x in range(NUMBEROFFRAMES):
        WAVEDATA = WAVEDATA + chr(int(math.sin(x / ((BITRATE / FREQUENCY) / math.pi)) * 127 + 128))

    for x in range(RESTFRAMES):
        WAVEDATA = WAVEDATA + chr(128)

    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1),
                    channels=1,
                    rate=BITRATE,
                    output=True)

    stream.write(WAVEDATA)
    stream.stop_stream()
    stream.close()
    p.terminate()


CHUNK = 4000
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.PyAudio()

chosen_device_index = 2
for x in range(0, p.get_device_count()):
    info = p.get_device_info_by_index(x)
    # print p.get_device_info_by_index(x)
    if info["name"] == "pulse":
        chosen_device_index = info["index"]
        print
        "Chosen index: ", chosen_device_index

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input_device_index=chosen_device_index,
                input=True,
                output=True,
                frames_per_buffer=CHUNK
                )

plt.ion()
fig, ax = plt.subplots()

x = np.arange(0, CHUNK)
data = stream.read(CHUNK)
data_int16 = struct.unpack(str(CHUNK) + 'h', data)
line, = ax.plot(x, data_int16)
# ax.set_xlim([xmin,xmax])
ax.set_ylim([-2 ** 15, (2 ** 15) - 1])

kontrol1 = 1

def calistir(kontrol,arduinodeger):
    if(kontrol==1):
        t1 = threading.Thread(target=sesUretme,args=[arduinodeger])
        t1.start()

while True:
    if (arduinoSerialData.inWaiting() > 0):
        myData = arduinoSerialData.readline().decode()
        myData = str(myData)
        myData = myData.replace(" ", "")
        deneme = int(myData, 16)
        ardudeger = deneme
        #print(ardudeger)
        calistir(kontrol1, ardudeger)
        kontrol1 += 1






    # myData = myData.replace("b'", "")
    # myData = myData.replace(r"\r\n'", "")

    # sonuc = int(myData, 2)
    # print(sonuc)

    # myData = random.randint(300, 1200)
    # sesUretme(myData)
    data = struct.unpack(str(CHUNK) + 'h', stream.read(CHUNK))
    line.set_ydata(data)
    fig.canvas.draw()
    fig.canvas.flush_events()
