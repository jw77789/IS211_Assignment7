import random

class Die:
    """ Numbered cube """
    
    def __init__(self, seed=0):
        random.seed(seed)  

    def roll(self):
        return random.randint(1, 6)


class Player:
    """ A Player in the game pig """
    
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        self.score += points

    def reset_score(self):
        self.score = 0


class Game:
    """ Determines how the game is played """

    def __init__(self):
        self.die = Die()
        self.players = [Player("Player 1"), Player("Player 2")]
        self.current_player = 0

    def switch_turn(self):
        self.current_player = 1 - self.current_player  

    def play_turn(self):
        player = self.players[self.current_player]
        turn_total = 0

        print(f"\n{player.name}'s turn. Current Score: {player.score}")

        while True:
            roll = self.die.roll()
            print(f"{player.name} rolled: {roll}")

            if roll == 1:
                print(f"{player.name} loses all points this turn!")
                turn_total = 0
                break
            else:
                turn_total += roll
                print(f"Turn total: {turn_total}, Game score: {player.score}")

                decision = input("Roll again (r) or Hold (h)? ").strip().lower()
                if decision == 'h':
                    break

        player.add_score(turn_total)
        print(f"{player.name}'s new score: {player.score}")
        self.switch_turn()

    def is_winner(self, player):
        return player.score >= 100

    def play_game(self):
        print("The Game of Pig.")

        while True:
            self.play_turn()
            if self.is_winner(self.players[self.current_player - 1]): 
                print(f"{self.players[self.current_player - 1].name} wins with {self.players[self.current_player - 1].score} points!")
                break


if __name__ == "__main__":
    game = Game()
    game.play_game()
