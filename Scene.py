class Scene:
    def __init__(self):
        self._game_objects = []
        
    def render(self, screen):
        for game_object in self._game_objects:
            game_object.render(screen)
            