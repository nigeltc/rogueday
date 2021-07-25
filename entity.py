"""
Genric dungeon entities
"""
import copy
from typing import Tuple

class Entity:
    """
    A generic dungeon Entity
    """

    gamemap = None
    
    def __init__(
            self,
            gamemap=None,
            x=0,
            y=0,
            char="@",
            color=(255, 255, 255),
            name="<Unamed>",
            blocks_movement=False):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement
        if gamemap:
            self.gamemap = gamemap
            gamemap.entities.add(self)

    def spawn(self, gamemap, x, y):
        """Spawn a copy of this entity at the given location."""
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        clone.gamemap = gamemap
        gamemap.entities.add(clone)
        return clone
        
    def place(self, x, y, gamemap=None):
        """
        Place this entity at a new location.
        Handles moving across GameMaps
        """
        self.x = x
        self.y = y
        if gamemap:
            if hasattr(self, "gamemap"): # Possibly uninitialized
                if self.gamemap:
                    self.gamemap.entities.remove(self)
            self.gamemap = gamemap
            gamemap.entities.add(self)
            

    def move(self, dx: int, dy: int) -> None:
        """Move the entity by a given  amount"""
        self.x += dx
        self.y += dy

    
