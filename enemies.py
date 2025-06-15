from Enemy import Enemy, EnemyAction
import pygame

class SkeletonSword(Enemy):
    def __init__(self, position=(0, 0)):
        super().__init__(max_health=15, shield=0, position=position, image="Sprites/Enemies/SkeletonSword/idle-1.png", hp_bar_offset= (50, 110))
        self.scale = (4, 4)  # Set the scale for the skeleton sword enemy
        self._animation_list = ["Sprites/Enemies/SkeletonSword/idle-1.png", "Sprites/Enemies/SkeletonSword/idle-2.png", "Sprites/Enemies/SkeletonSword/idle-3.png", "Sprites/Enemies/SkeletonSword/idle-4.png"]
        self._current_frame = 0
        self.set_actions(
            [
                EnemyAction("damage", 5, 5),
                EnemyAction("shield", 3, 1)
            ]
        )

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
        super().__init__(max_health=20, shield=15, position=position, image="Sprites/Enemies/SkeletonShield/idle-1.png", hp_bar_offset= (50, 100))
        self.scale = (4, 4)
        self._animation_list = ["Sprites/Enemies/SkeletonShield/idle-1.png", "Sprites/Enemies/SkeletonShield/idle-2.png", "Sprites/Enemies/SkeletonShield/idle-3.png", "Sprites/Enemies/SkeletonShield/idle-4.png"]
        self._current_frame = 0
        self.set_actions(
            [
                EnemyAction("damage", 5, 5),
                EnemyAction("shield", 3, 1)
            ]
        )

    def update(self):
        super().update()
        self._current_frame += 0.01
        if self._current_frame >= len(self._animation_list):
            self._current_frame = 0
        self.image = self._animation_list[int(self._current_frame)]
        self.image = pygame.transform.flip(self._image, True, False)
        self.scale = (4, 4)

class Shadow(Enemy):
    def __init__(self, position=(0, 0)):
        super().__init__(max_health=10, shield=5, position=position, image="Sprites/Enemies/Shadow/idle-1.png", hp_bar_offset= (0, 120))
        self.scale = (4, 4)
        self._animation_list = ["Sprites/Enemies/Shadow/idle-1.png", "Sprites/Enemies/Shadow/idle-2.png", "Sprites/Enemies/Shadow/idle-3.png", "Sprites/Enemies/Shadow/idle-4.png"]
        self._current_frame = 0
        self.set_actions(
            [
                EnemyAction("damage", 5, 5),
                EnemyAction("shield", 3, 1)
            ]
        )

    def update(self):
        super().update()
        self._current_frame += 0.01
        if self._current_frame >= len(self._animation_list):
            self._current_frame = 0
        self.image = self._animation_list[int(self._current_frame)]
        self.image = pygame.transform.flip(self._image, True, False)
        self.scale = (4, 4)
