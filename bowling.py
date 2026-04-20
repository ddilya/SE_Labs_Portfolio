class Game:
    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)

    def score(self):
        total_score = 0
        roll_index = 0
        for frame in range(10):
            if self._is_spare(roll_index):
                total_score += 10 + self._rolls[roll_index + 2]
                roll_index += 2
            else:
                total_score += self._rolls[roll_index] + self._rolls[roll_index + 1]
                roll_index += 2
        return total_score

    def _is_spare(self, roll_index):
        return self._rolls[roll_index] + self._rolls[roll_index + 1] == 10