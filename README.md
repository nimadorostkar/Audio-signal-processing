# Audio-signal-processing
audio signal processing using Python and covers concepts such as real-time voice recording, transcription, encryption and decryption.



![example](https://github.com/nimadorostkar/Audio-signal-processing/blob/main/Figure_1%20Hello%20world%20waveform.png)


~transcribe.py file is a program that converts speech to text in real time

~capture a microphone input.py is a program that loads a wavefile object and plots its `waveform` using Matplotlib and Numpy libraries

~microphone input code.py capture a microphone input in `real time` using specified parameters, stores the recorded data in a wavefile object, `transcribes` it then `encrypts` it by generating an encryption key. The encrypted data is also `decrypted` uisng a decryption key.

~import pyaudio.py loads a stored wave audio format file and produces te following audio signal parameters: 

        `Number of channels i.e. mono for single channel and stereo for two channels`
        
        `Sample width`
        
        `Frame rate/sample rate`
        
        `Number of frames`
        
        `Value of a frame`
