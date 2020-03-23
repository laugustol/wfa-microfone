"""import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone(device_index=0) as source:
    audio = r.listen(source)
    
try:
    print("You said " + r.recognize_google(audio))
except LookupError:
    print("Could not understand audio")"""
import audioop,math
from threading import Timer
import pyaudio
import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://192.168.1.7:8080')





CHUNK = 1024
p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16,
        channels = 1,
        rate = 44100,
        input = True,
        frames_per_buffer = CHUNK)
cont = 0




while 1:

    data = stream.read(CHUNK)
    rms = audioop.rms(data,2)
    decibel = 20 * math.log10(rms)
    if(decibel > 63):
    	cont = cont + 1
    	print("AQU"+ str(int(decibel))+ " "+ str(cont))	
    	sio.emit('ledTwo')
    	if(cont == 2):
    		print("AQUIIIIIII "+ str(int(decibel))+ " "+ str(cont))	
    	

