"""
Fighter component
"""
from .base_component import BaseComponent
import color
from input_handlers import GameOverEventHandler
from render_order import RenderOrder

class Fighter(BaseComponent):
    parent = None
    
    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self._hp = hp
        self.defense = defense
        self.power = power

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, min(value, self.max_hp))
        if self.hp == 0 and self.parent.ai:
            self.die()

    def die(self):
        if self.engine.player is self.parent:
            death_message = "You died!"
            death_message_color = color.player_die
            self.engine.event_handler = GameOverEventHandler(self.engine)
        else:
            death_message = f"{self.parent.name} is dead."
            death_message_color = color.enemy_die
        self.parent.char = "%"
        self.parent.color = (191, 0, 0)
        self.parent.blocks_movement = False
        self.parent.ai = None
        self.parent.name = f"remains of {self.parent.name}"
        self.parent.render_order = RenderOrder.CORPSE
        self.engine.message_log.add_message(death_message, death_message_color)

    def heal(self, amount):
        if self.hp == self.max_hp:
            return 0

        new_hp = self.hp + amount
        if new_hp > self.map_hp:
            new_hp = self.max_hp

        amount = new_hp - self.hp
        self.hp = new_hp

        return amount

    def take_damage(self, amount):
        self.hp -= amount
    
    
