from ollama import ChatResponse, chat, ResponseError
from app import play 
import threading, time, sys


def get_response(prompt):
    stop_event = threading.Event()
    t = threading.Thread(target=spinner, args=(stop_event, "Generating response"))
    t.start()

    try:
        response: ChatResponse = chat(
            model="wizardlm2",
            messages=prompt
        )
    except ResponseError as e:
        match e.status_code:
            case 404:
                play.end("Model not installed, call \'ollama pull wizardlm2\'")
            case _: print(f"ERROR: {e.error}")
    else:
        return response['message']['content']
    finally:
        stop_event.set()
        t.join()


def spinner(stop_event, message):
    while not stop_event.is_set():
        for char in "|/-\\":
            sys.stdout.write(f"\r{message}... {char}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write(f"\r{(' ') * 25}\n")
