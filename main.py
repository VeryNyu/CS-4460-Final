from app.play import Play
from app.logic import Logic
from app.model import Model


def main():

    print("Hello, World!")
    FLAG = "SECRET123"
    while True:
        user_input = Play.get_input()
        AIResponse = Model.get_response(user_input)
        print(AIResponse)
        user_input = input("Enter the password: ")
        if Logic.check_password(user_input, FLAG):
            print("Correct password! Access granted.")
            break
        else:
            print("Incorrect password. Try again.")
    

if __name__ == "__main__":
    main()