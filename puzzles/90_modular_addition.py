name = "Modular Addition"

def get_problem(self, difficulty):
    x = self.generate_number(difficulty)
    y = self.generate_number(difficulty)
    y = abs(y) + 1
    question = "%s %% %s" % (x, y)
    answer = x % y
    return question, answer