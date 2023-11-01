import random
import sys
from colorama import Fore, Back, init, Style
import os
import time
from configurations import *


class Game:
    def __init__(self):
        self.theme = random.choice(list(WORDS.keys()))
        self.words = WORDS[self.theme]
        self.attempts = ATTEMPTS
        self.hangman = HANGMAN
        self.victory = VICTORY
        self.congrats = CONGRATS

    def draw_hangman(self):
        word = [i for i in random.choice(self.words)]
        spaces = ["_ " for i in word]
        while self.attempts > 0:
            if word == spaces:
                sys.stdout.write("Checking the results")
                for _ in range(10):
                    sys.stdout.write(".")
                    sys.stdout.flush()
                    time.sleep(0.5)
                os.system('cls')
                print(self.congrats)
                time.sleep(1)
                os.system('cls')
                print(self.victory[0])

                break
            player_input = input("THEME: {}"
                                 "{} \n"
                                 "Word: {} \n"
                                 "Letter: "
                                 "".format(self.theme,
                Fore.GREEN + self.hangman[::-1][self.attempts] + Style.RESET_ALL,
                                           ''.join([i for i in spaces]))
                                 ).capitalize()
            if player_input in word:
                for i in range(len(word)):
                    if word[i] == player_input:
                        spaces[i] = word[i]

            else:
                self.attempts -= 1
            os.system('cls')
            if self.attempts == 0:
                os.system('cls')
                print(Fore.RED + self.hangman[-1])


if __name__ == '__main__':
    game = Game()
    game.draw_hangman()
