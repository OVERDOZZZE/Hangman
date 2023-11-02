import os
import random
import time
from colorama import Fore as F, Back, Style as S


class Game:
    def __init__(self):
        self.boss = Boss()
        self.heroes_lst = ['Berserk', 'Archer', 'Wizard']
        self.lives = 2
        self.heroes = [Berserk(self.boss), Archer(self.boss), Wizard(self.boss)]
        # self.gamer = input('What is your name, stranger? \n'
        #                    'Name: ')
        self.character = None
        self.limit = 3

    def start(self):
        try:
            choice = int(input(f'\nChoose your character:\n'
                                f'1.{self.heroes_lst[0]}\n'
                               f'2.{self.heroes_lst[1]} \n'
                               f'3.{self.heroes_lst[2]} \n'
                               f'Choice: '))
            if self.heroes_lst[choice-1] == 'Dead':
                print('The character already died!')
                self.start()
            self.character = self.heroes[choice-1]
            self.boss.enemy = self.character
            while self.character.health > 0:
                os.system('cls')
                print(f'{self.boss.__class__.__name__}: {F.GREEN + str(self.boss.health)} hp'
                      + S.RESET_ALL)
                print(f'{self.character.__class__.__name__}: {F.GREEN + str(self.character.health)} hp'
                      + S.RESET_ALL)
                try:
                    attack = int(input('\n1.Attack   2. Superpower \n\n'))
                except ValueError:
                    print('No no no ts ts!')
                    time.sleep(1)
                    continue
                if attack == 1:
                    self.character.attack()
                    if self.limit < 3:
                        self.limit += 1
                    print(F.YELLOW + f'\nYou have damaged'
                                        f' {self.character.damage} hp!' + S.RESET_ALL)
                    time.sleep(2)
                elif attack == 2 and self.limit == 3:
                    self.limit -= 1
                    self.character.super_ability()
                    time.sleep(2)
                else:
                    print('\nNo no no ts ts !')
                    time.sleep(2)
                    continue
                if self.boss.health > 0:
                    self.boss.attack()
                else:
                    print('You won!')
                    break
            if self.character.health < 1:
                os.system('cls')
                if self.lives > 0:
                    print('Your character lose, choose the new one')
                    self.heroes_lst[choice-1] = (F.RED + 'Dead' + S.RESET_ALL)
                    self.lives -= 1
                    self.start()
                else:
                    print('You totally lose!')
        except:
            raise ValueError


class Character:
    def __init__(self, damage, health, enemy=None):
        self.damage = damage
        self.health = health
        self.enemy = enemy

    def attack(self):
        self.enemy.health -= self.damage

    def super_ability(self):
        pass


class Berserk(Character):
    def __init__(self, enemy):
        super().__init__(10, 150, enemy)

    def super_ability(self):
        super_damage = self.damage * random.randint(2, 5)
        self.enemy.health -= super_damage
        print(F.MAGENTA + f'\nSuper-Damage: {super_damage}!' + S.RESET_ALL)


class Archer(Character):
    def __init__(self, enemy):
        super().__init__(25, 70, enemy)

    def super_ability(self):
        heal = random.randint(10, 35)
        self.health += heal
        print(F.GREEN + f"\nYou've healed {heal} hp!" + S.RESET_ALL)


class Wizard(Character):
    def __init__(self, enemy):
        super().__init__(30, 70, enemy)

    def super_ability(self):
        debuff = random.randint(2, 5)
        if self.enemy.damage > 3:
            self.enemy.damage -= debuff
            print(F.CYAN + f'\nDebuff on enemy - {debuff}' + S.RESET_ALL)
        else:
            self.enemy.health -= self.damage * 2
            print(F.CYAN + f'\nSpell-Damage: {self.damage * 2}' + S.RESET_ALL)


class Boss(Character):
    def __init__(self, enemy=None):
        super().__init__(15, 500, enemy=enemy)


if __name__ == '__main__':
    game = Game()
    game.start()
