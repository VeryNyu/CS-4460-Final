from app.play import Play
from app.logic import Logic
from app.model import Model


def main():
    print("Hello, World!")
    while True:
        user_input = Play.get_input()
        print(f"You entered: {user_input}")
    

if __name__ == "__main__":
    main()