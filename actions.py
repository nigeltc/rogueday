"""
Game actions
"""
import color
import exceptions

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


class ItemAction(Action):
    def __init__(self, entity, item, target_xy=None):
        super().__init__(entity)
        self.item = item
        if not target_xy:
            target_xy = entity.x, entity.y
        self.target_xy = target_xy

    @property
    def target_actor(self):
        """Return the actor at this action's destination"""
        return self.engine.game_map.get_actor_at_location(*self.target_xy)

    def perform(self):
        self.item.consumable.activate(self)
    

class EscapeAction(Action):
    """ESC Action"""

    def perform(self):
        raise SystemExit()

class WaitAction(Action):
    def perform(self):
        pass
    
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

    @property
    def target_actor(self):
        """Return the actor at this action's destination."""
        return self.engine.game_map.get_actor_at_location(*self.dest_xy)

    def perform(self):
        raise NotImplementedError()
    

class MeleeAction(ActionWithDirection):
    def perform(self):
        target = self.target_actor
        if not target:
            raise exceptions.Impossible("Nothing to attack.")
        damage = self.entity.fighter.power - target.fighter.defense
        attack_desc = f"{self.entity.name.capitalize()} attacks {target.name}"
        if self.entity is self.engine.player:
            attack_color = color.player_atk
        else:
            attack_color = color.enemy_atk
        if damage > 0:
            self.engine.message_log.add_message(
                f"{attack_desc} for {damage} hit points.",
                attack_color)
            target.fighter.hp -= damage
        else:
            self.engine.message_log.add_message(
                f"{attack_desc} but does no damage",
                attack_color)
        
    
class MovementAction(ActionWithDirection):
    """Player movement"""

    def perform(self):
        dest_x, dest_y = self.dest_xy

        if not self.engine.game_map.in_bounds(dest_x, dest_y):
            # destination is out of bounds
            raise exceptions.Impossible("That way is blocked.")
        if not self.engine.game_map.tiles["walkable"][dest_x, dest_y]:
            # destination is blocked
            raise exceptions.Impossible("That way is blocked.")
        if self.engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            # destination is blocked by an entity
            raise exceptions.Impossible("That way is blocked.")
        self.entity.move(self.dx, self.dy)


class BumpAction(ActionWithDirection):
    def perform(self):
        if self.target_actor:
            return MeleeAction(self.entity, self.dx, self.dy).perform()
        else:
            return MovementAction(self.entity, self.dx, self.dy).perform()


