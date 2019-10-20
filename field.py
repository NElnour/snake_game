from __future__ import annotations
from snake import Snake
import pygame
from pygame.locals import *
import sys


class Field:
    """A field class represents the state of the field
    It also updates and displays the field
    The size of a field is 300 x 300 and each grid should have size 10 x 10
    === Attributes ===
    _snake: an instance of snake in the field
    _appleX: a x coordinate of an apple in the field
    _appleY: a y coordinate of an apple in the field
    """
    _snake: Snake
    _appleX: int
    _appleY: int

    def __init__(self):
        """Initialize a field
        """
        self._snake = Snake()
        self._appleX, self._appleY = 200, 200
        self.display_field()

    def display_field(self) -> None:
        """Draw the state of the field
        Clear the field first and create a new field
        TODO: add a method body and write a doctest
        """
        pass

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
        pass

    def _draw_snake_body(self) -> None:
        """Draw a block representing a snake's body
        TODO: add a method body and write a doctest
        """
        pass

    def _create_apple(self) -> None:
        """Randomly generate an apple on the field such that
        it does not appear inside the field and not on the snake's body
        TODO: add a method body and write a doctest
        """
        pass

    def _draw_apple(self) -> None:
        """Draw an apple on the field
        TODO: add a method body and write a doctest
        """
        pass

    def get_snake_head(self) -> tuple:
        """Return location of snake head on board
        TODO: add a method body and write a doctest
        """
        pass

    def get_snake_tail(self) -> tuple:
        """Return location of snake tail on board
        TODO: add a method body and write a doctest
        """
        pass
