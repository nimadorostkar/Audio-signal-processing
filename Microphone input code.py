import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import speech_recognition as sr
from cryptography.fernet import Fernet
import pyaudio

#Capture a microphone input with specified parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p= pyaudio.PyAudio()

stream= p.open(format= FORMAT, channels= CHANNELS, rate= RATE, input= True, frames_per_buffer=CHUNK)
#prompt the user to start recording
print ("Start recording...")

frames=[]
seconds= 3 #three seconds time lapse before recording stops
for i in range(0, int(RATE/ CHUNK* seconds)):
    data=stream.read(CHUNK)
    frames.append(data)
print ("recording stopped") 

stream.stop_stream()
stream.close()
p.terminate()

#store data in the micinput wavefile
wf= wave.open("micinput.wav", 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()


#Transcription
filename = "micinput.wav"
# initialize the recognizer
r = sr.Recognizer()
# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)

#Encryption
#Generating the encryption key
key = Fernet.generate_key()

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)

#loading the encryption key
with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

print(key)

#Encrypting the file
f = Fernet(key) #We initialize the Fernet object as store is as a local variable f

with open('micinput.wav', 'rb') as original_file:
    original = original_file.read()  #Next, we read our original data (Hello world.wav) into original

encrypted = f.encrypt(original) #Then we encrypt the data using the Fernet object and store it as encrypted

with open ('enc_micinput.wav', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)  #And finally, we write it into a new .wav file file called “enc_Hello world.wav”

#Decrypting the file
f = Fernet(key)

with open('enc_micinput.wav', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('dec_micinput.wav', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)

#END