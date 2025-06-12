import pygame
from GameObject import GameObject
from Text import Text

class Button(GameObject):
    def __init__(self, position, height: int, width: int, background_color=(0,0,255), button_text=None, font_size=30, font_color=(255, 255, 255), font_path=None, image_path=None, on_click=None):
        super().__init__(position, image_path=image_path, on_click=on_click)
        self._height = height
        self._width = width
        self._background_color = background_color
        self._position = position
        self.check_hover = True
        self.rect = pygame.Rect(
            self._position[0],
            self._position[1],
            self._width,
            self._height
        )
        self.rect.center = (self._position[0], self._position[1])
        self.text = Text((0, 0), button_text, font_size, font_color, font_path) if button_text else None
        if self.text is not None:
            self.add_child(self.text)
        self.button_text = button_text
        
    @property
    def height(self):
        return self._height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
        self.rect.width = value
        self.rect.center = (self._position[0], self._position[1])

    def render(self, screen):
        if self._image:
            image_rect = self._image.get_rect(center=self.rect.center)
            screen.blit(self._image, image_rect)
        else:
            pygame.draw.rect(screen, self._background_color, self.rect)
        for c in self.children:
            c.update_relative_position()
            c.render(screen)
