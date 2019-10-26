import pygame
from pygame.locals import *
import sys
from field import Field
from snake import Snake


class Game:
    """ Game class controls the flow of the game.
    This class receives inputs from users and pass the inputs to other classes
    to update the state of a field.
    === Attributes ===
    _field: an instance of a field class representing a game field.
    """

    def __init__(self, l:int, w:int) -> None:
        """Initializes a snake class and field class
        TODO: write a doctest
        """
        self.dim = (l, w)
        self.board = pygame.Rect(0, 0, l, w)
        self._field = Field()

    def main(self) -> None:
        """ run the game. The loop continues until
        either the snake hits the wall or eats his tail.
        TODO: add a method body and write a doctest
        """
        while not self._is_game_over():
            self._run_game()

    def _is_game_over(self) -> bool:
        """ check the state of a field and return true
        if the game over condition is met.
        TODO: add a method body and write a doctest
        """

        boundaries = [(0, 0),
                      (0, self.dim[0]),
                      (0, self.dim[1]),
                      self.dim]

        if self._field.get_snake_head() in boundaries or \
                self._field.get_snake_head() == self._field.get_snake_tail():
            return True

        return False

    @staticmethod
    def _run_game() -> None:
        """ recursively call this method until the game is over.
        This method should receive user inputs and update state of a field
        TODO: add a method body and write a doctest
        """

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            elif event.type == KEYDOWN:
                pass

        # clear scrren
        # update screen

        # check if snake hit boundaries -- > yes = goto end game; no = draw

        # check if snake ate its tail -- > yes = goto end game; no = draw


if __name__ == "__main__":
    game = Game()
    game.main()
