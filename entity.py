"""
Genric dungeon entities
"""
import copy
from typing import Tuple

class Entity:
    """
    A generic dungeon Entity
    """
    def __init__(
            self,
            x: int = 0,
            y: int = 0,
            char: str = "@",
            color: Tuple[int, int, int] = (255, 255, 255),
            name: str = "<Unamed>",
            blocks_movement: bool = False):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement

    def spawn(self, gamemap, x: int, y: int):
        """Spawn a copy of this entity at the given location."""
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        gamemap.entities.add(clone)
        return clone
        

    def move(self, dx: int, dy: int) -> None:
        """Move the entity by a given  amount"""
        self.x += dx
        self.y += dy

    
