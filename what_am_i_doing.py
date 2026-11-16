class damn:
    def __init__(self, word):
        self.word = word
    def damn(self):
        return "damn" + self.word
    def __repr__(self):
        return "damn {0}".format(self.word)
    def __str__(self):
        return f"damn {self.word}"
damndamn = damn("damn damn")
