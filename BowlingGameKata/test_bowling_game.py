import unittest
from bowling_game import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def roll_many(self, n, pins):
        for _ in range(n):
            self.game.roll(pins)

    def test_gutter_game(self):
        self.roll_many(20, 0)
        self.assertEqual(self.game.score(), 0)

    def test_all_ones(self):
        self.roll_many(20, 1)
        self.assertEqual(self.game.score(), 20)

    def test_one_spare(self):
        self.game.roll(5)
        self.game.roll(5) 
        self.game.roll(3)
        self.roll_many(17, 0)
        self.assertEqual(self.game.score(), 16)

    def test_one_strike(self):
        self.game.roll(10) 
        self.game.roll(3)
        self.game.roll(4)
        self.roll_many(16, 0)
        self.assertEqual(self.game.score(), 24)

    def test_perfect_game(self):
        self.roll_many(12, 10)
        self.assertEqual(self.game.score(), 300)

    def test_invalid_roll(self):
        with self.assertRaises(ValueError):
            self.game.roll(-1)