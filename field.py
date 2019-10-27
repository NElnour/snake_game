from __future__ import annotations

import random

import pygame

from snake import Snake


class Field:
    """A field class represents the state of the field
    It also updates and displays the field
    The size of a field is 300 x 300 and each grid should have size 10 x 10
    === Attributes ===
    -snake: an instance of snake in the field
    _appleX: a x coordinate of an apple in the field
    _appleY: a y coordinate of an apple in the field
    """

    _snake: Snake
    _appleX: int
    _appleY: int

    def __init__(self, game_surface):
        """Initialize a field
        """
        self.window = game_surface
        self._snake = Snake()
        self._appleX, self._appleY = 200, 200
        self.display_field()

    def display_field(self) -> None:
        """Draw the state of the field
        Clear the field first and create a new field
        TODO: write a doctest
        """
        self.window.fill((255, 255, 255))  # clear field
        self._draw_snake()
        self._draw_apple()
        pygame.display.flip()

    def _clear_field(self) -> None:
        """Clear the field and generate new field
        TODO: add a method body and write a doctest
        """
        pass

    def _draw_snake(self) -> None:
        """Draw a snake body on the field.
        This method iterate snake's body and
        call 'draw_snake_body_parts' to draw it on the field
        """
        snake_list = self._snake.get_body_coordinates()
        for i in snake_list:
            pygame.draw.rect(self.window, (0, 0, 0),
                             (i[0] * 10, i[1] * 10, 10, 10))

    def _draw_snake_body(self) -> None:
        """Draw a block representing a snake's body
        TODO: add a method body and write a doctest
        """
        pass

    def create_apple(self) -> None:
        """Randomly generate an apple on the field such that
        it does not appear inside the field and not on the snake's body
        TODO:  write a doctest
        """

        loop_condition = True
        snake_list = self.snake.get_body_coordinates()
        while loop_condition:
            temp_X = random.randint(0, 30)
            temp_Y = random.randint(0, 30)
            for i in snake_list:  # Check temp coordinates not in snake
                if temp_X != i[0] and temp_Y != i[1]:
                    loop_condition = False

    def _draw_apple(self) -> None:
        """Draw an apple on the field
        TODO: write a doctest
        """
        pygame.draw.rect(self.window, (255, 0, 0), (self._appleX * 10,
                                                    self._appleY * 10, 10, 10))

    def get_snake_head(self) -> tuple:
        """Return location of snake head on board
        TODO: write a doctest
        """
        return self._snake.get_head()

    def get_snake_tail(self) -> tuple:
        """Return location of snake tail on board
        TODO: write a doctest
        """
        return self._snake.get_coordinates()[-1]
