from typing import Tuple

import numpy as np

# Tile Graphics - character, fg colour, bg colour
graphic_dt = np.dtype(
    [
        ("ch", np.int32), # unicode codepoint
        ("fg", "3B"),     # 3 bytes
        ("bg", "3B")      # 3 bytes
    ]
)

# Tile - tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool),    # True if tile can be walked over
        ("transparent", np.bool), # True if this tile doesn't block FoV
        ("dark", graphic_dt),     # Graphics for when this tile is not in FoV
        ("light", graphic_dt)     # Graphics for when this tile is in FoV
    ]
)

def new_tile(
        *,  # Enforce the use of keywords
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
        light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]]
        ) -> np.ndarray:
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)

SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

floor = new_tile(walkable=True,
                 transparent=True,
                 dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
                 light=(ord(" "), (255, 255, 255), (200, 180, 50)))

wall = new_tile(walkable=False,
                transparent=False,
                dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
                light=(ord(" "), (255, 255, 255), (130, 110, 50)))


