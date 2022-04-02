from game import Game

def main():
    new_game = Game()
    #Add players for Game
    new_game.add_players()
    print("User Added: ")
    new_game.show_players()
    new_game.start_game()


if __name__ == "__main__":
    main()