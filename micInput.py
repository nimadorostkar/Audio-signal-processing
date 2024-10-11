import wave 
import numpy as np 
import matplotlib.pyplot as plt 
import speech_recognition as sr
from pydub import AudioSegment
from cryptography.fernet import Fernet

file= wave.open('.wav') #loading the wavefile

print('number of channels',file.getnchannels()) #gives number of channels in audio file:1 for mono, 2 for stereo
print('sample width',file.getsampwidth()) #gives number of bits per sample
print('frame rate',file.getframerate()) #gives the sampling frquency/sample rate/frame rate
print('Number of frames',file.getnframes()) #returns number of frames

n_channels=file.getnchannels() #Defining the assignments
s_width=file.getsampwidth()
f_rate=file.getframerate()
n_frames=file.getnframes()
print('Value of a frame',n_channels*16)

data=file.readframes(-1) #read data from all the frames
w_data=np.frombuffer(data,np.int16) #obtain data as a numpy array of integers
print(w_data)
w_data.shape= -1,2 #restructuring the numpy array into two columns, first column containing data from first channel;second column from second channel
print(w_data.shape)
w_data=w_data.T #obtains the transpose, first row contains data from first channel, second row contains data from second channel
print(w_data)
duration_data=n_frames/float(f_rate) #formula to obtain length of audiofile
increment=1/float(f_rate) #formula to obtain the incremental rate
t_seq= np.arange(0,duration_data,increment) #generates a time sequence
plt.plot(t_seq,w_data[0]) #plot time sequence against data for specified channel
plt.title('waveform of wavefile')
plt.show()

# transcribe audio file                                                         
AUDIO_FILE = "micinput2.wav"

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file                  

print("Transcription: " + r.recognize_google(audio))

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

with open('Hello world.wav', 'rb') as original_file:
    original = original_file.read()  #Next, we read our original data (Hello world.wav) into original

encrypted = f.encrypt(original) #Then we encrypt the data using the Fernet object and store it as encrypted

with open ('enc_Hello world.wav', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)  #And finally, we write it into a new .wav file file called “enc_Hello world.wav”

#Decrypting the file
f = Fernet(key)

with open('enc_Hello world.wav', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('dec_Hello world.wav', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)

#END