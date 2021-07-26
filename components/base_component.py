"""
Components attached to entities
"""


class BaseComponent:
    entity = None

    @property
    def engine(self):
        return self.entity.gamemap.engine

    @property
    def gamemap(self):
        return self.entity.gamemap

    
