from typing import Callable
import pygame
import globals
from pygame.math import Vector2

class GameObject(pygame.sprite.Sprite):
    def __init__(self, position=(0,0), image_path=None, on_click: Callable | None = None):
        super().__init__()
        self.visible: bool = True 
        self.rect = None
        self.position = position
        self._children = []
        self._parent: GameObject | None = None
        self._image = None
        self.position = position
        self._scale = Vector2(1, 1)  # Default scale
        self.original_size = (0,0) # used for scaling
        # if true, GameObject reacts on mouse hover
        self.check_hover = False
        if image_path:
            self.image = image_path
        self._on_click = on_click
    
    # position relative to parent
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value: Vector2 | list | tuple):
        if isinstance(value, list) or isinstance(value, tuple):
            if len(value) != 2:
                raise ValueError("Position must be a list or tuple of length 2")
            self._position = Vector2(value)
        elif isinstance(value, Vector2):
            self._position = value
        if self.rect is not None:
            self.rect.center = int(self.global_position[0]), int(self.global_position[1]) 
            
    # position on screen 
    @property
    def global_position(self):
        if self._parent:
            return self._parent.global_position + self.position
        return self.position

    @global_position.setter
    def global_position(self, value: Vector2 | list | tuple):
        if hasattr(self, 'verbose'):
            if self.verbose:
                print(f"Setting global position: {value}")
        if not isinstance(value, Vector2):
            if len(value) != 2:
                raise ValueError("Position list must be of length 2")
            value = Vector2(value)
        if self.parent is None:
            self.position = value
        else:
            self.position = Vector2(value.x - self.parent.global_position.x, value.y - self.parent.global_position.y)

    @property
    def image(self):
        return self._image
    
    @image.setter
    def image(self, path: str | pygame.Surface):
        if isinstance(path, str):
            self._image = pygame.image.load(path)
        elif isinstance(path, pygame.Surface):
            self._image = path
        self.original_size = self._image.get_size()
        self.rect = self._image.get_rect()
        self.rect.center = int(self.global_position[0]), int(self.global_position[1])
    
    @property
    def parent(self):
        return self._parent
    
    @property
    def children(self):
        return self._children
    
    def add_child(self, child: 'GameObject'):
        self._children.append(child)
        child._parent = self

            
    def render(self, screen):
        if self.parent is not None:
            self.rect.center = int(self.global_position[0]), int(self.global_position[1])
        if not self.visible:
            return
        if self.rect is not None:
            screen.blit(self._image, self.rect)
        for child in self._children:
            child.render(screen)
    
    @property
    def scale(self):
        return self._scale
    
    @scale.setter
    def scale(self, value):
        if isinstance(value, (list, tuple)):
            if len(value) != 2:
                raise ValueError("Scale must be a list or tuple of length 2")
            self._scale = Vector2(value)
        elif isinstance(value, Vector2):
            self._scale = value
        else:
            raise ValueError("Scale must be a list, tuple or Vector2")
        if self.rect is not None and self.image is not None:
            self.image = pygame.transform.scale(self.image, (self.original_size[0] * self._scale.x, self.original_size[1] * self._scale.y))
            self.rect.center = int(self.global_position[0]), int(self.global_position[1])
        

    def check_collision(self, position):
        if self.rect is None:
            return False
        else:
            return self.rect.collidepoint(position)


    def update(self):
        # check if collides with mouse
        if self.check_hover:
            coll = self.check_collision(globals.mouse_position)
            if coll:
                globals.current_scene.hovered_item = self

    def on_hover_enter(self):
        pass
    def on_hover_exit(self):
        pass

    def click(self):
        if self._on_click is None:
            return
        if callable(self._on_click):
            self._on_click()
            print(f"Clicked on {self.__class__.__name__} at {self.global_position}")
        else:
            raise TypeError("on_click is not callable")
