from speech_recognition import Recognizer, Microphone, UnknownValueError


def get_verbal_input():
    r = Recognizer()
    print(Microphone.list_microphone_names())
    mic = Microphone(device_index=0)
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
try:
    result = r.recognize_google(audio)
except UnknownValueError:
    result = ""
    return result

if __name__ == "__main__":
    x = get_verbal_input()
    print(x)