from __future__ import annotations

from typing import List, Tuple


class Snake:
    """A snake consists of multiple snake nodes.
    His body has length of 4 at the beginning.
    When he eats an apple, his head is added front.
    When he hits the wall or eats his tail, the game is over.

    === Attributes ===
    _head: represents snake's head. this must be the first element in _body
    _body: represents snake's body
    _dx: horizontal velocity of snake's body
    _dy: vertical velocity of snake's body
    _direction: handle snake's direction
    """
    head: SnakeNode
    body: List[SnakeNode]
    _dx: int
    _dy: int
    _direction: str

    def __init__(self):
        """Initialize snake's body.
        The snake initially moves to the right.
        TODO: add doctests
        """
        self._body = [SnakeNode(150, 150 - i * 10) for i in range(5)]
        self._head = self._body[0]
        self._dx, self.dy = 10, 0

    def move(self) -> Tuple[int, int]:
        """Returns new location at which snake's head moves.
        TODO: add doctests and method body
        """
        pass

    def change_direction(self):
        """Change snake's direction based on a given input.
        The snake should not be able to go backward.
        For example, if he is moving to the right, he has to take 2 steps
        in order to turn left(move top and then move left for instance).
        TODO: add doctests and method body
        """
        pass

    def get_body_coordinates(self) -> List[SnakeNode]:
        """Returns the snake's head"""
        return self.body

    def get_head(self) -> SnakeNode:
        """Returns the snake's head"""
        return self.head


class SnakeNode:
    """Snake node represents each part of his body

    === Attribute ===
    x: x-coordinate of this node
    y: y-coordinate of this node
    """

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def get_coordinates(self) -> Tuple[int, int]:
        """returns tuple of x and y coordinate"""
        return self.x, self.y
