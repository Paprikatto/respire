from GameObject import GameObject


class Scene:
    def __init__(self):
        self._game_objects = []
        
    def render(self, screen):
        for game_object in self._game_objects:
            game_object.render(screen)
            
    def add_object(self, game_object):
        if not isinstance(game_object, GameObject):
            raise ValueError("Object must be a GameObject")
        self._game_objects.append(game_object)
            