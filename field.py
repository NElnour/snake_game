from __future__ import annotations

import random
from typing import Tuple, Optional

import pygame

from snake import Snake

COLOR_WHITE = (255, 255, 255)


class Field:
    """A field class represents the state of the field
    It also updates and displays the field
    The size of a field is 300 x 300 and each grid should have size 10 x 10
    === Attributes ===
    _snake: an instance of snake in the field
    _appleX: a x coordinate of an apple in the field
    _appleY: a y coordinate of an apple in the field
    _apple_is_eaten: if apple is eaten by snake
    """
    _snake: Snake
    _apple_X: Optional[int]
    _apple_Y: Optional[int]
    _apple_is_eaten: bool

    def __init__(self, game_surface: pygame.Surface):
        """Initialize a field
        """
        self.window = game_surface
        self._snake = Snake()
        self._apple_X, self._apple_Y = None, None
        self._apple_is_eaten = False

    def display_field(self) -> None:
        """Draw the state of the field
        Clear the field first and create a new field
        TODO: write a doctest
        """
        self.window.fill(COLOR_WHITE)  # clear field

        # initialize game view
        self._clear_field()

        self._draw_snake()
        self._create_apple()
        self._draw_apple()

    def _clear_field(self) -> None:
        """Clear the field and generate new field
        TODO: add a method body and write a doctest
        """
        self.window.fill((0, 0, 80))
        pygame.draw.rect(self.window, (0, 0, 0), (150, 150, 300, 300))

    def _draw_snake(self) -> None:
        """Draw a snake body on the field.
        This method iterate snake's body and
        call 'draw_snake_body_parts' to draw it on the field
        """

        snake_list = self._snake.get_body_coordinates()
        for i in snake_list:
            pygame.draw.rect(self.window, (0, 0, 0),
                             (i[0] * 10, i[1] * 10, 10, 10))

        # get all snake bodies and then draw each
        snake_bodies = self._snake.get_bodies()
        for body in snake_bodies:
            self._draw_snake_body(body.get_coordinates())

    def _draw_snake_body(self, body: Tuple[int, int]) -> None:
        """Draw a block representing a snake's body
        TODO: add a method body and write a doctest
        """
        body_rect = (body[0] + 1, body[1] + 1, 8, 8)
        pygame.draw.rect(self.window, (0, 255, 0), body_rect)

    def _create_apple(self) -> None:
        """Randomly generate an apple on the field such that
        it does not appear inside the field and not on the snake's body
        TODO:  write a doctest
        """

        loop_condition = True
        snake_list = [self._snake.get_head()] + \
                     self._snake.get_bodies()
        while loop_condition:
            temp_X = random.randint(0, 30)
            temp_Y = random.randint(0, 30)
            for i in snake_list:  # Check temp coordinates not in snake
                if temp_X != i[0] and temp_Y != i[1]:
                    if self._apple_is_eaten:
                        self._apple_X, self._apple_Y = \
                            self._generate_random_coor()
                        self._apple_is_eaten = False
                    elif self._apple_X is None and self._apple_Y is None:
                        self._apple_X, self._apple_Y = \
                            self._generate_random_coor()

    def _generate_random_coor(self) -> Tuple[int, int]:
        """Returns a random coordinate such that
        it does not overlap snake body"""
        temp_x = 0
        temp_y = 0
        loop_condition = True
        snake_bodies = self._snake.get_bodies()
        while loop_condition:
            temp_x = random.randint(0, 30) * 10
            temp_y = random.randint(0, 30) * 10
            for body_node in snake_bodies:  # Check temp coordinates not in
                # snake
                body = body_node.get_coordinates()
                if temp_x != body[0] and temp_y != body[1]:
                    loop_condition = False
        return temp_x, temp_y

    def _draw_apple(self) -> None:
        """Draw an apple on the field
        TODO: write a doctest
        """

        pygame.draw.rect(self.window, (255, 0, 0), (self._apple_X * 10,
                                                    self._apple_Y * 10, 10, 10))

        apple_rect = (150 + self._apple_X + 1, 150 + self._apple_Y + 1, 8, 8)
        pygame.draw.rect(self.window, (255, 0, 0), apple_rect)

    def get_snake_head(self) -> Tuple[int, int]:
        """Return location of snake head on board
        TODO: write a doctest
        """
        head_node = self._snake.get_head()
        return head_node.get_coordinates()

    def get_snake_tail(self) -> Tuple[int, int]:
        """Return location of snake tail on board
        TODO: write a doctest
        """

        tail_node = self._snake.get_bodies()[-1]
        return tail_node.get_coordinates()
