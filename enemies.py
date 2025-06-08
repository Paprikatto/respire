from Enemy import Enemy
import pygame

class SkeletonSword(Enemy):
    def __init__(self, position=(0, 0)):
        super().__init__(name="Skeleton Sword", max_health=100, armor=10, position=position, image_path="Sprites/Enemies/SkeletonSword/idle-1.png")
        self.scale = (4, 4)  # Set the scale for the skeleton sword enemy
        self._animation_list = ["Sprites/Enemies/SkeletonSword/idle-1.png", "Sprites/Enemies/SkeletonSword/idle-2.png", "Sprites/Enemies/SkeletonSword/idle-3.png", "Sprites/Enemies/SkeletonSword/idle-4.png"]
        self._current_frame = 0

    def update(self):
        super().update()
        self._current_frame += 0.01
        if self._current_frame >= len(self._animation_list):
            self._current_frame = 0
        self.image = self._animation_list[int(self._current_frame)]
        self.image = pygame.transform.flip(self._image, True, False)
        self.scale = (4, 4)

class SkeletonShield(Enemy):
    def __init__(self, position=(0, 0)):
        super().__init__(name="Skeleton Shield", max_health=120, armor=15, position=position, image_path="Sprites/Enemies/SkeletonShield/idle-1.png")
        self.scale = (4, 4)
        self._animation_list = ["Sprites/Enemies/SkeletonShield/idle-1.png", "Sprites/Enemies/SkeletonShield/idle-2.png", "Sprites/Enemies/SkeletonShield/idle-3.png", "Sprites/Enemies/SkeletonShield/idle-4.png"]
        self._current_frame = 0

    def update(self):
        super().update()
        self._current_frame += 0.01
        if self._current_frame >= len(self._animation_list):
            self._current_frame = 0
        self.image = self._animation_list[int(self._current_frame)]
        self.image = pygame.transform.flip(self._image, True, False)
        self.scale = (4, 4)


