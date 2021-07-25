"""
Game actions
"""
#from engine import Engine
#from entity import Entity

class Action:
    """Base action"""
    def __init__(self, entity):
        super().__init__()
        self.entity = entity

    @property
    def engine(self):
        """Return the engine this action belongs to"""
        return self.entity.gamemap.engine
    
    def perform(self):
        """
        Perform this action. 
        self.entity.gamemap.ENGINE is the scope for the action
        self.ENTITY is the object performing the action
        """
        raise NotImplementedError()


class EscapeAction(Action):
    """ESC Action"""

    def perform(self):
        raise SystemExit()

    
class ActionWithDirection(Action):
    def __init__(self, entity, dx, dy):
        super().__init__(entity)
        self.dx = dx
        self.dy = dy

    @property
    def dest_xy(self):
        """Return the action's destination."""
        return self.entity.x + self.dx, self.entity.y + self.dy

    @property
    def blocking_entity(self):
        """Return the blocking entity at the action's destination."""
        return self.engine.game_map.get_blocking_entity_at_location(*self.dest_xy)

    def perform(self):
        raise NotImplementedError()
    

class MeleeAction(ActionWithDirection):
    def perform(self):
        target = self.blocking_entity
        if not target:
            return
        print(f"You kick the {target.name}, much to its annoyance.")
        
    
class MovementAction(ActionWithDirection):
    """Player movement"""

    def perform(self):
        dest_x, dest_y = self.dest_xy

        if not self.engine.game_map.in_bounds(dest_x, dest_y):
            # destination is out of bounds
            return
        if not self.engine.game_map.tiles["walkable"][dest_x, dest_y]:
            # destination is blocked
            return
        if self.engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            # destination is blocked by an entity
            return
        self.entity.move(self.dx, self.dy)


class BumpAction(ActionWithDirection):
    def perform(self):
        if self.blocking_entity:
            return MeleeAction(self.entity, self.dx, self.dy).perform()
        else:
            return MovementAction(self.entity, self.dx, self.dy).perform()


