import unittest
from game import Game
from unittest.mock import patch


class GameSelectionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.game = Game()

    def test_select_dead(self):
        for i in self.game.heroes:
            i.health = 0
        with self.assertRaises(ValueError):
            self.game.start()


class GameFightTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.game = Game()



