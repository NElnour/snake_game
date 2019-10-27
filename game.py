import pygame
from pygame.locals import *
from pygame.time import Clock
from typing import Tuple, Optional
import sys
from field import Field


class Game:
    """ Game class controls the flow of the game.
    This class receives inputs from users and pass the inputs to other classes
    to update the state of a field.
    === Attributes ===
    _field: an instance of a field class representing a game field.
    _
    """
    # Attributes
    _dim: Tuple[int, int]
    _in_game: bool
    _menu_index: int
    _field: Optional[Field]

    def __init__(self, l: int, w: int) -> None:
        """Initializes a snake class and field class"""
    # Constants
    COLOR_WHITE = (255, 255, 255)
    TITLE_SCREEN_COLOR = (0, 0, 80)

    def __init__(self) -> None:
        """Initializer of game class
        Field class will be generated in main method
        TODO: write a doctest
        """
        self._dim = (400, 400)
        self._in_game = False
        self._menu_index = 0
        self._field = None

    def main(self) -> None:
        """ run the game. The loop continues until
        either the snake hits the wall or eats his tail.
        TODO: write a doctest
        """
        # Initialize pygame, generate screen and field
        pygame.init()
        screen = self._init_screen()
        clock = pygame.time.Clock()
        fps = 30
        while True:
            if not self._in_game:
                self._display_title_screen(screen)
            else:
                self._run_game(screen)
            clock.tick(fps)

    def _init_screen(self) -> pygame.Surface:
        """Initialize title screen"""
        screen = pygame.display.set_mode((600, 600))
        screen.fill(self.TITLE_SCREEN_COLOR)
        pygame.display.set_caption("Snake game")
        self._menu_index = 0
        self._field = Field(screen)
        return screen

    def _clear_title_screen(self, screen: pygame.Surface) -> None:
        """Clear title screen and draw title and menu options"""
        screen.fill(self.TITLE_SCREEN_COLOR)
        title_font = pygame.font.SysFont("monospace", 80)
        title_label = title_font.render("Snake game", 1, (255, 255, 255))
        screen.blit(title_label, (130, 100))
        # create title select
        self._create_menu_label(screen, "Play", (270, 300))
        self._create_menu_label(screen, "Score", (270, 360))
        self._create_menu_label(screen, "Quit", (270, 420))

    def _display_title_screen(self, screen: pygame.Surface) -> None:
        """Draw menu option arrow and update view"""
        # Clear current view contents
        self._clear_title_screen(screen)
        # Receive user inputs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                self._menu_selection_handler(event.type)
        # Draw menu selection arrow
        self._draw_menu_selection_arrow(screen, [300, 360, 420][self._menu_index])
        pygame.display.update()

    def _menu_selection_handler(self, key_value: int) -> None:
        """Handle key inputs in title screen"""
        if key_value == pygame.K_UP:
            self._menu_index -= 1
            if self._menu_index < 0:
                self._menu_index = 2
        elif key_value == pygame.K_DOWN:
            self._menu_index += 1
            if self._menu_index > 2:
                self._menu_index = 0
        elif key_value == pygame.K_RETURN:
            if self._menu_index == 0:
                self._in_game = True
            elif self._menu_index == 0:
                # TODO add score view
                pass
            else:
                pygame.quit()
                sys.exit()

    def _create_menu_label(self, screen: pygame.Surface, label_text: str, location: Tuple[int, int]) -> None:
        """Draw menu label from given label text at given location"""
        menu_font = pygame.font.SysFont("monospace", 40)
        menu_label = menu_font.render(label_text, 1, self.COLOR_WHITE)
        screen.blit(menu_label, location)

    def _draw_menu_selection_arrow(self, screen: pygame.Surface, y_location: int) -> None:
        """Draw menu selection arrow into screen"""
        menu_arrow_location = [[200, y_location + 2], [200, y_location + 22], [220, y_location + 12]]
        pygame.draw.polygon(screen, self.COLOR_WHITE, menu_arrow_location)

    def _is_game_over(self) -> bool:
        """ check the state of a field and return true
        if the game over condition is met.
        TODO: and write a doctest
        """
        boundaries = [(0, 0),
                      (0, self._dim[0]),
                      (0, self._dim[1]),
                      self._dim]

        if self._field.get_snake_head() in boundaries or \
                self._field.get_snake_head() == self._field.get_snake_tail():
            return True

        return False

    def _run_game(self) -> None:
        """ recursively call this method until the game is over.
        This method should receive user inputs and update state of a field
        TODO: add a method body and write a doctest
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # TODO pass key event to snake or field to draw
                self._field.display_field()


# clear screen
# update screen

# check if snake hit boundaries -- > yes = goto end game; no = draw

# check if snake ate its tail -- > yes = goto end game; no = draw


if __name__ == "__main__":
    game = Game()
    game.main()
