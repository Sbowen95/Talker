from speech_recognition import Recognizer, Microphone
from os import system
from spotify_local import SpotifyLocal

def get_verbal_input() -> str:
    listener = Recognizer()
    # print(Microphone.list_microphone_names())
    mic = Microphone(device_index=0)
    with mic as source:
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)
    result = listener.recognize_google(audio)
    return result


def set_of_commands() -> set:
    return {
        "open", "status"
    }


def get_commands(v_input: str) -> str:
    v_command = ""
    words = v_input.split(" ")
    for word in words:
        if word == "music":
            v_command = word
    return v_command

def open_spotify():
    system("open /Applications/Spotify.app")
    print("opening Spotify")

def run_command(v_command: str):
    if v_command == "open":
        open_spotify()
    elif v_command == "status":
        with SpotifyLocal() as s:
             print(s.get_current_status())


if __name__ == "__main__":
    verbal_input = get_verbal_input()
    command = get_commands(verbal_input)
    print(command)
    run_command(command)
