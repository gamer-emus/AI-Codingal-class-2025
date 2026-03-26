import queue

import sounddevice as sd

from vosk import Model,KaldiRecognizer

import json



model = Model("/Users/ayaansharma/Desktop/Newfolder/Model")
recognizer = KaldiRecognizer(model,16000)


q = queue.Queue()


def callback(indata,frames,time,status):
    q.put(bytes(indata))

with sd.RawInputStream(samplerate=16000,blocksize=8000,dtype='int16',channels=1,callback=callback):
    print("Speak...")

    while True:
        data = q.get()


        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            print(result["text"])


