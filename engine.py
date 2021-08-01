"""
Engine to handle drawing and input
"""
from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console
from tcod.map import compute_fov

from entity import Entity
from game_map import GameMap
from input_handlers import MainGameEventHandler
from message_log import MessageLog
from render_functions import render_bar, render_names_at_mouse_location

class Engine:
    gamemap = None
    
    def __init__(self, player):
        self.event_handler = MainGameEventHandler(self)
        self.message_log = MessageLog()
        self.mouse_location = (0, 0)
        self.player = player

    def handle_enemy_turns(self):
        for entity in self.game_map.entities - {self.player}:
            if entity.ai:
                entity.ai.perform()
        
    def update_fov(self) -> None:
        """Recompute the visible area based on theplayer's PoV"""
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=8)
        # add visible tiles to explored
        self.game_map.explored |= self.game_map.visible
        
            
    def render(self, console):
        self.game_map.render(console)
        self.message_log.render(console=console, x=21, y=45,width=40, height=5)
        render_bar(console=console,
                   current_val=self.player.fighter.hp,
                   max_val=self.player.fighter.max_hp,
                   total_width=20)
        render_names_at_mouse_location(console=console, x=21, y=44,engine=self)

