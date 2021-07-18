import numpy as np
from tcod.console import Console
import tile_types

class GameMap:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

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
        

    
