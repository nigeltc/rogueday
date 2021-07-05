"""
Game actions
"""
#from engine import Engine
#from entity import Entity

class Action:
    """Base action"""

    #def perform(self, engine: Engine, entity: Entity) -> None:
    def perform(self, engine, entity):
        """
        Perform this action. 
        ENGINE is the scope for the action
        ENTITY is the object performing the action
        """
        raise NotImplementedError()


class EscapeAction(Action):
    """ESC Action"""

    def perform(self, engine, entity):
        raise SystemExit()
    

class MovementAction(Action):
    """Player movement"""
    def __init__(self, dx: int,dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy

    def perform(self, engine, entity):
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if not engine.game_map.in_bounds(dest_x, dest_y):
            # destination is out of bounds
            return
        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            # destination is blocked
            return
        entity.move(self.dx, self.dy)
