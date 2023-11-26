from collections.abc import Iterable
from catanatron import Game, RandomPlayer, Color
from catanatron.models.actions import Action, ActionType
from catanatron.models.player import Player

class MyPlayer(Player):
   def decide(self, game: Game, playable_actions: Iterable[Action]):
      """Should return one of the playable_actions.

      Args:
            game (Game): complete game state. read-only.
            playable_actions (Iterable[Action]): options to choose from
      Return:
            action (Action): Chosen element of playable_actions
      """
      return playable_actions[0]


print(ActionType)

# # Play a simple 4v4 game
# players = [
#     MyPlayer(Color.RED),
#     RandomPlayer(Color.BLUE),
#     RandomPlayer(Color.WHITE),
#     RandomPlayer(Color.ORANGE),
# ]
# game = Game(players)
# print(game.play())  # returns winning color