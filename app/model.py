from ollama import ChatResponse, chat, generate
from . import logic


def init():
    print("Warming model...")
    generate(model="wizardlm2")
    print("Model ready.")

def run():
    logic.execute_plays()


def get_response(user_input, prompt):

    response: ChatResponse = chat(
        model="wizardlm2",
        messages=[
        {
            'role': 'system',
            'content': prompt
        },
        {
            'role': 'user',
            'content': user_input
        }
        ]
    )

    return response['message']['content']
