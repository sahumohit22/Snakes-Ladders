from player import Player
from snake import Snake
from ladder import Ladder
import random

WINING_POSITION = 30

class Game:

    def __init__(self) -> None:
        self.player_list = []

    def add_players(self):
        print("Add Players for a New Game")
        player_count = int(input("Enter Number of Players: "))
        for num in range(player_count):
            username = input(f"Eneter {num+1} UserName: ")
            player_obj = Player(username)
            self.player_list.append(player_obj)
    
    def show_players(self):
        print(f'{len(self.player_list)} Playing...')
        for player in self.player_list:
            print(player.username)
    
    def start_game(self):
        CONTINUE = True
        print("Starting Game...")
        round_number = 0
        while CONTINUE:
            round_number += 1
            print(f'====================< {round_number} >========================')
            for player in self.player_list:
                print(f'-> {player.username} turn')
                input("throw dice -- <press Enter>") 
            
                #Generate Random Number b/w 1 and 6
                dice = random.randint(1, 6)
                print(f'    it is {dice}')
                six_count = 0
                sum = dice
                while dice == 6:
                    input(f'    Got {dice}, throw again -- <press Enter>')
                    dice = random.randint(1, 6)
                    print(f'    it is {dice}')
                    six_count += 1
                    sum += dice
                    if six_count == 2:
                        print('    Consecutive 3 Six are allow')
                        break
                temp_position = player.position + sum
                if Snake.is_present(temp_position):
                    print("    Hiss.... snake bites")
                    dest = Snake.get_destination(temp_position)
                    print(f'    you fall to {dest}')
                    player.position = dest
                elif Ladder.is_present(temp_position):
                    print("    Bravo.... You found ladder")
                    dest = Ladder.get_destination(temp_position)
                    print(f'    you climb to {dest}')
                    player.position = dest
                else:
                    dest = temp_position
                print(f'    your Latest Position is {dest}')
                player.position = dest
                if dest >= WINING_POSITION:
                    print(f'    Hurray {player.username} win...')
                    CONTINUE = False
                    break