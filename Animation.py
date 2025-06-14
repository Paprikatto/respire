from GameObject import GameObject
import pygame

class Animation(GameObject):
    
    def __init__(self, frames: list[str], position: tuple[int,int] = (0, 0),
                 animation_speed:float = 0.25, one_shot: bool = True, play_on_start: bool = False, scale: tuple[int,int] = (1,1)):
        super().__init__(position)
        self._frames = []
        self.current_frame = 0
        self.animation_speed = animation_speed
        self.one_shot = one_shot
        for f in frames:
            img = pygame.image.load(f)
            img = pygame.transform.scale(img, (img.get_width() * scale[0], img.get_height() * scale[1]))
            self._frames.append(img)
        self.image = self._frames[0]
        if not play_on_start:
            self.visible = False
            
    def play(self):
        self.visible = True
            
    def render(self, screen):
        super().render(screen)
        if not self.visible:
            return
        self.current_frame += self.animation_speed
        rounded_frame = int(self.current_frame)
        if rounded_frame >= len(self._frames):
            self.current_frame = 0
            rounded_frame = 0
            if self.one_shot:
                self.visible = False
        self._image = self._frames[rounded_frame]
        
        
         
            
            
            