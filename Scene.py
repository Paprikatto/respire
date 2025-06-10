from GameObject import GameObject


class Scene:
    def __init__(self):
        self._game_objects = []
        self.hovered_item: GameObject | None = None
        self.prev_hovered_item: GameObject | None = None 
    def render(self, screen):
        self.hovered_item = None
        for game_object in self._game_objects:
            game_object.render(screen)
            game_object.update()
            
    def add_object(self, game_object):
        if not isinstance(game_object, GameObject):
            raise ValueError("Object must be a GameObject")
        self._game_objects.append(game_object)
            
