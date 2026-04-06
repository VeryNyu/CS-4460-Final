from os.path import join, dirname, abspath
import json


def build_prompt(user_input):
    with open(join(dirname(abspath(__file__)), 'config/rules.json'), 'r') as f:
        rules = json.load(f)

    prompt = rules['system_prompt']

    system_message =[
        {
            'role': 'system',
            'content': prompt
        },
        {
            'role': 'user',
            'content': user_input
        }
    ]

    return system_message

def check_password(user_input, correct_password):
    return user_input == correct_password