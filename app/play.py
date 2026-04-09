from . import logic
from time import sleep


def init():
    print('''
      ___       __   __         ___   /         
|  | |__  |    /  ` /  \  |\/| |__   /          
|/\| |___ |___ \__, \__/  |  | |___ .           
                                                
___         __        __          __        __  
 |  |__| | /__`    | /__`    \ / /  \ |  | |__) 
 |  |  | | .__/    | .__/     |  \__/ \__/ |  \ 
                                                
 __        __   __        __   __   __          
|__)  /\  /__` /__` |  | /  \ |__) |  \         
|    /~~\ .__/ .__/ |/\| \__/ |  \ |__/         
                                                
                      __   ___  __              
 |\/|  /\  |\ |  /\  / _` |__  |__)             
 |  | /~~\ | \| /~~\ \__> |___ |  \             
                                                
''')


def run():
    print("You can start chatting with the AI. To guess the password, Type \'/\', then take your guess. Type 'exit' to stop.")
    while True:
        user_input = get_input()

        if user_input.lower() == "exit":
            end()
        elif user_input.startswith('/'):
            guess = user_input[1:].strip()
            logic.check_password(guess)
        else:
            logic.build_prompt(user_input)


def get_input():
    return input("You: ")


def end(s="Thank you for playing!"):
    print(s)
    for i in range(3):
        print(".", end='', flush=True)
        sleep(1)
    print("Goodbye!")
    exit(0)