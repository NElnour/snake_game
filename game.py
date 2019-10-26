import pygame
from pygame.locals import *
from pygame.time import Clock
from typing import Tuple
import sys
from field import Field
from snake import Snake



class Game:
    """ Game class controls the flow of the game.
    This class receives inputs from users and pass the inputs to other classes
    to update the state of a field.
    === Attributes ===
    _field: an instance of a field class representing a game field.
    _
    """
    # Constants
    COLOR_WHITE = (255, 255, 255)

    def __init__(self, height: int, width: int) -> None:
        """Initializes a snake class and field class
        TODO: write a doctest
        """
        self.dim = (height, width)
        self.board = pygame.Rect(0, 0, height, width)
        self._field = Field()
        self._in_game = False
        self._menu_index = 0

    def main(self) -> None:
        """ run the game. The loop continues until
        either the snake hits the wall or eats his tail.
        TODO: write a doctest
        """
        screen = self.init_screen()
        clock = pygame.time.Clock()
        fps = 30
        while True:
            if not self._in_game:
                self._display_title_screen(screen)
            else:
                self._run_game(screen)
            clock.tick(fps)

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

    def init_screen(self) -> pygame.Surface:
        """Initialize title screen"""
        pygame.init()
        screen = pygame.display.set_mode((600, 600))
        screen.fill((0, 0, 128))
        pygame.display.set_caption("Snake game")
        self._menu_index = 0
        return screen

    def _init_title_screen(self, screen: pygame.Surface) -> None:
        screen.fill((0, 0, 0))
        title_font = pygame.font.SysFont("monospace", 80)
        title_label = title_font.render("Snake game", 1, (255, 255, 255))
        screen.blit(title_label, (130, 100))
        # create title select
        self._create_menu_label(screen, "Play", (270, 300))
        self._create_menu_label(screen, "Score", (270, 360))
        self._create_menu_label(screen, "Quit", (270, 420))

    def _display_title_screen(self, screen: pygame.Surface) -> None:
        self._init_title_screen(screen)
        menu_y_coordinates = [300, 360, 420]
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_UP:
                    self._menu_index -= 1
                    if self._menu_index < 0:
                        self._menu_index = 2
                if event.key == pygame.K_DOWN:
                    self._menu_index += 1
                    if self._menu_index > 2:
                        self._menu_index = 0

        self._create_menu_label_arrow(screen, menu_y_coordinates[self._menu_index])
        pygame.display.update()

    def _create_menu_label(self, screen: pygame.Surface, label_text: str, location: Tuple[int, int]) -> None:
        menu_font = pygame.font.SysFont("monospace", 40)
        menu_label = menu_font.render(label_text, 1, self.COLOR_WHITE)
        screen.blit(menu_label, location)

    def _create_menu_label_arrow(self, screen: pygame.Surface, location_y: int) -> None:
        pygame.draw.polygon(screen, self.COLOR_WHITE, [[200, location_y + 2], [200, location_y + 22], [220, location_y + 12]])

    @staticmethod
    def _run_game(screen: pygame.Surface) -> None:
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
    game = Game(100, 100)
    game.main()
