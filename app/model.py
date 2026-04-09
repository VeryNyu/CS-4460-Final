from ollama import ChatResponse, chat
import threading, time, sys


def get_response(prompt):
    stop_event = threading.Event()
    t = threading.Thread(target=spinner, args=(stop_event, "Generating response"))
    t.start()

    response: ChatResponse = chat(
        model="wizardlm2",
        messages=prompt
    )

    stop_event.set()
    t.join()
    return response['message']['content']


def spinner(stop_event, message):
    while not stop_event.is_set():
        for char in "|/-\\":
            sys.stdout.write(f"\r{message}... {char}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write(f"\rDone!{(' ') * 20}\n")