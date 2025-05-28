from tkinter.tix import IMAGE

import pygame
from pygame.math import Vector2
class GameObject(pygame.sprite.Sprite):
    def __init__(self, position=(0,0), image_path=None):
        super().__init__()
        self.rect = None
        self.position = position
        self._children = []
        self._parent = None
        self._image = None
        self.position = position
        self._scale = Vector2(1, 1)  # Default scale
        self.original_size = (0,0)
        if image_path:
            self.image = image_path
            
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
        else:
            raise ValueError("Position must be a list, tuple or Vector2")
        if self.rect is not None:
            self.rect.center = int(self.global_position[0]), int(self.global_position[1]) 
        
    @property
    def image(self):
        return self._image
    
    @image.setter
    def image(self, path: str | pygame.Surface):
        if isinstance(path, str):
            self._image = pygame.image.load(path)
        elif isinstance(path, pygame.Surface):
            self._image = path
        else:
            raise ValueError("Image path must be a string")
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
        if not isinstance(child, GameObject):
            raise ValueError("Child must be a GameObject")
        self._children.append(child)
        child._parent = self
    
    @property
    def global_position(self):
        if self._parent:
            return self._parent.global_position + self.position
        return self.position
            
    def render(self, screen):
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
        if self.rect is not None:
            self.image = pygame.transform.scale(self.image, (self.original_size[0] * self._scale.x, self.original_size[1] * self._scale.y))
            self.rect.center = int(self.global_position[0]), int(self.global_position[1])
        