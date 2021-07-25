from typing import Iterable
import numpy as np
from tcod.console import Console
import tile_types

class GameMap:
    def __init__(self, engine, width, height, entities=()):
        self.engine = engine
        self.width = width
        self.height = height
        self.entities = set(entities)

        # create the actual map 
        self.tiles = np.full((width, height),
                             fill_value=tile_types.wall,
                             order="F")

        # visible tiles
        self.visible = np.full((width, height),
                               fill_value=False,
                               order="F")

        # explored tiles
        self.explored = np.full((width, height),
                                fill_value=False,
                                order="F")


    def get_blocking_entity_at_location(self, location_x, location_y):
        for entity in self.entities:
            if entity.blocks_movement and (entity.x == location_x) and (entity.y == location_y):
                return entity
        return None
    
            
    def in_bounds(self, x: int, y: int) -> bool:
        """True if (x,y) is in bounds"""
        return (0 <= x < self.width) and (0 <= y < self.height)

    def render(self, console: Console) -> None:
        """
        Render the map
        If a tile is in the "visible" array, then draw th "light" colours.
        If it isn't, but it's in the "explored" array, then draw it with the "dark" colour,
        Otherwise the default is SHROUD
        """
        console.tiles_rgb[0:self.width, 0:self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tile_types.SHROUD)

        for entity in self.entities:
            # only render entities that are in the FOV
            if self.visible[entity.x, entity.y]:
                console.print(entity.x, entity.y, entity.char, fg=entity.color)


    
