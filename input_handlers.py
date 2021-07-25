"""
Convert input into actions
"""
from typing import Optional
import tcod.event
from actions import Action, BumpAction, EscapeAction

class EventHandler(tcod.event.EventDispatch[Action]):
    def __init__(self, engine):
        self.engine = engine

    def handle_events(self):
        for event in tcod.event.wait():
            action = self.dispatch(event)
            if action is None:
                continue
            action.perform()

            # handle enemy turns & update FoV before player's next action
            self.engine.handle_enemy_turns()
            self.engine.update_fov()


    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None
        player = self.engine.player

        key = event.sym
        if key == tcod.event.K_UP:
            action = BumpAction(player, dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = BumpAction(player, dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = BumpAction(player, dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = BumpAction(player, dx=1, dy=0)
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction(player)

        return action
            
