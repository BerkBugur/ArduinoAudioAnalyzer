# ArduinoAudioAnalyzer
Arduino'da üretilen random ses frekansının ses kartına aktarılıp canlı olarak görüntülenmesi 
 
 Gereksinimler:
 Sanal Ses Girişiyle üretmek istiyorsanız:
 https://vb-audio.com/Cable/ indirip kodta input_device_index kısmını değiştirmeniz gerekiyor.
 Arduino daki seri haberleşme portunu kendinize göre ayarlamalısınız.
 A0 pinini boş bıraklamısınız randomseed üretiliyor.
 
 Buzzer ile ses üretme:
 D3 pini ve gnd pinine buzzerı bağlayın
 input_device_index kısmını -1 olarak default ayarlayın
 
 Python Terminal:
 pip install pyaudio
 Hata alırsanız:pip install pipwin , pipwin install pyaudio
 pip install struct
 pip install serial
 pip install matplotlib.pyplot
 pip install numpy
 
 
