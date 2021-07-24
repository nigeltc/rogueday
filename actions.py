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

    
class ActionWithDirection(Action):
    def __init__(self, dx, dy):
        super().__init__()
        self.dx = dx
        self.dy = dy

    def perform(self, engine, entity):
        raise NotImplementedError()
    
class MeleeAction(ActionWithDirection):
    def perform(self, engine, entity):
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy
        target = engine.game_map.get_blocking_entity_at_location(dest_x, dest_y)
        if not target:
            return
        print(f"You kick the {target.name}, much to its annoyance.")
        
    
class MovementAction(ActionWithDirection):
    """Player movement"""

    def perform(self, engine, entity):
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if not engine.game_map.in_bounds(dest_x, dest_y):
            # destination is out of bounds
            return
        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            # destination is blocked
            return
        if engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            # destination is blocked by an entity
            return
        entity.move(self.dx, self.dy)

class BumpAction(ActionWithDirection):
    def perform(self, engine, entity):
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy
        target = engine.game_map.get_blocking_entity_at_location(dest_x, dest_y)
        if target:
            return MeleeAction(self.dx, self.dy).perform(engine, entity)
        else:
            return MovementAction(self.dx, self.dy).perform(engine, entity)


