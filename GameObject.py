import pygame
from pygame.math import Vector2
class GameObject:
    def __init__(self, position=(0,0), image_path=None):
        self.position = position
        self._children = []
        self._parent = None
        self._image = None
        if image_path:
            self._image = pygame.image.load(image_path)
            
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if isinstance(value, list) or isinstance(value, tuple):
            if len(value) != 2:
                raise ValueError("Position must be a list or tuple of length 2")
            value = Vector2(value)
        elif isinstance(value, Vector2):
            self._position = value
        else:
            raise ValueError("Position must be a list, tuple or Vector2")
        
    @property
    def image(self):
        return self._image
    
    @image.setter
    def image(self, path):
        if not isinstance(path, str):
            raise ValueError("Image path must be a string")
        self._image = pygame.image.load(path)
    
    @property
    def parent(self):
        return self._parent
    
    @property
    def children(self):
        return self._children
    
    def add_child(self, child):
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
        if self._image is not None:
            screen.blit(self._image, self.global_position)
        for child in self._children:
            child.render(screen)
    
        