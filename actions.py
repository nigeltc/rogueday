"""
Game actions
"""

class Action:
    """Base action"""
    pass

class EscapeAction(Action):
    """ESC Action"""
    pass

class MovementAction(Action):
    """Player movement"""
    def __init__(self, dx: int,dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy
