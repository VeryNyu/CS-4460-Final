from ollama import ChatResponse, chat, generate


def init():
    print("Warming model...")
    generate(model="wizardlm2")
    print("Model ready.")


def get_response(prompt):
    response: ChatResponse = chat(
        model="wizardlm2",
        messages=prompt
    )
    return response['message']['content']
