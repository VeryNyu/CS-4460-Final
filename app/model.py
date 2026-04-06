class Model(object):
    def __init__(self, logic):
        self.logic = logic

    def run(self):
        self.logic.execute_plays()