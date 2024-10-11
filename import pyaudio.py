import pyaudio
import wave
import speech_recognition as sr
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p= pyaudio.PyAudio()

stream= p.open(format= FORMAT, channels= CHANNELS, rate= RATE, input= True, frames_per_buffer=CHUNK)

print ("Start recording...")

frames=[]
seconds= 6
for i in range(0, int(RATE/ CHUNK* seconds)):
    data=stream.read(CHUNK)
    frames.append(data)
print ("recording stopped") 

stream.stop_stream()
stream.close()
p.terminate()

wf= wave.open("micinput4.wav", 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

