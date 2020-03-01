import subprocess

command = "ffmpeg -i test.mp4 -ab 160k -ac 2 -ar 44100 -vn audio.wav"

subprocess.call(command, shell=True)



import speech_recognition as sr

r = sr.Recognizer()

PATH = 'audio.wav'

with sr.AudioFile(PATH) as source:
	audio = r.record(source)

captions = r.recognize_google(audio)

print(captions)

f = open("captions.txt", "w")
f.write(captions)


# import speech_recognition as sr
# r = sr.Recognizer()
# with sr.WavFile("audio.wav") as source:              # use "test.wav" as the audio source
#     audio = r.record(source)                        # extract audio data from the file

# try:
#     print("Transcription: " + r.recognize(audio))   # recognize speech using Google Speech Recognition
# except LookupError:                                 # speech is unintelligible
#     print("Could not understand audio")