from speech_recognition import Recognizer, Microphone
r = Recognizer()
print(Microphone.list_microphone_names())
mic = Microphone(device_index=0)
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
result = r.recognize_google(audio)
print(result)

