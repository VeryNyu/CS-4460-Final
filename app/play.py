class Play(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def play(self):
        print(f"Playing {self.name}: {self.description}")
    
    def get_input():
        return input("Try talking to the AI: ")