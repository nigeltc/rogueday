import actions
import color
from components.base_component import BaseComponent
from exceptions import Impossible

class Consumable(BaseComponent):
    parent = None

    def get_action(self, consumer):
        """Return the action for this item."""
        return actions.ItemAction(consimer, self.parent)

    def activate(self, action):
        """Invoke this item's ability."""
        raise NotImplementedError()

class HealingConsumable(Consumable):
    def __init__(self, amount):
        self.amount = amount

    def activate(self, action):
        consumer = action.entity
        recovered = consumer.fighter.heal(self.amount)
        if recovered > 0:
            self.engine.message_log.add_message(
                f"You consume the {self.parent.name}, and recover {recovered} HP!",
                color.health_recovered)
        else:
            raise Impossible("Your health is already full.")
    
