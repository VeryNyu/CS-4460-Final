class Logic(object):
    def __init__(self):
        self.plays = []

    def add_play(self, play):
        self.plays.append(play)

    def execute_plays(self):
        for play in self.plays:
            play.play()