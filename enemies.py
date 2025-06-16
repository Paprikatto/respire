from Enemy import Enemy, EnemyAction, get_stat
import pygame

class SkeletonSword(Enemy):
    DAMAGE = [4, 4, 5, 5, 5, 6, 6, 7]
    SHIELD_AMOUNT = [3, 3, 3, 3, 4, 4, 5]
    def __init__(self, position=(0, 0)):
        super().__init__(max_health=15, shield=0, position=position, image="Sprites/Enemies/SkeletonSword/idle-1.png", hp_bar_offset= (50, 110))
        self.scale = (4, 4)  # Set the scale for the skeleton sword enemy
        self._animation_list = ["Sprites/Enemies/SkeletonSword/idle-1.png", "Sprites/Enemies/SkeletonSword/idle-2.png", "Sprites/Enemies/SkeletonSword/idle-3.png", "Sprites/Enemies/SkeletonSword/idle-4.png"]
        self._current_frame = 0
        self.set_actions(
            [
                EnemyAction("damage", get_stat(SkeletonSword.DAMAGE, self.battle_index) , 5),
                EnemyAction("shield", get_stat(SkeletonSword.SHIELD_AMOUNT, self.battle_index), 1)
            ]
        )

    def update(self):
        super().update()
        self._current_frame += 0.015
        if self._current_frame >= len(self._animation_list):
            self._current_frame = 0
        self.image = self._animation_list[int(self._current_frame)]
        self.image = pygame.transform.flip(self._image, True, False)
        self.scale = (4, 4)

class SkeletonShield(Enemy):
    DAMAGE = [3, 3, 3, 3, 4, 4, 4, 5]
    SHIELD_AMOUNT = [4, 4, 5, 5, 5, 6, 6]
    def __init__(self, position=(0, 0)):
        super().__init__(max_health=20, shield=15, position=position, image="Sprites/Enemies/SkeletonShield/idle-1.png", hp_bar_offset= (50, 100))
        self.scale = (4, 4)
        self._animation_list = ["Sprites/Enemies/SkeletonShield/idle-1.png", "Sprites/Enemies/SkeletonShield/idle-2.png", "Sprites/Enemies/SkeletonShield/idle-3.png", "Sprites/Enemies/SkeletonShield/idle-4.png"]
        self._current_frame = 0
        self.set_actions(
            [
                EnemyAction("damage", get_stat(SkeletonShield.DAMAGE, self.battle_index) , 3),
                EnemyAction("shield", get_stat(SkeletonShield.SHIELD_AMOUNT, self.battle_index), 1)
            ]
        )

    def update(self):
        super().update()
        self._current_frame += 0.015
        if self._current_frame >= len(self._animation_list):
            self._current_frame = 0
        self.image = self._animation_list[int(self._current_frame)]
        self.image = pygame.transform.flip(self._image, True, False)
        self.scale = (4, 4)

class Shadow(Enemy):
    DAMAGE = [2, 2, 3, 3, 4, 5]
    SHIELD_AMOUNT = [2, 2, 3, 3, 3, 4, 5]
    HEALTH = [10, 12, 15, 15, 20, 20, 30]
    def __init__(self, position=(0, 0)):
        super().__init__(max_health=get_stat(Shadow.HEALTH), shield=5, position=position, image="Sprites/Enemies/Shadow/idle-1.png", hp_bar_offset= (0, 120))
        self.scale = (4, 4)
        self._animation_list = ["Sprites/Enemies/Shadow/idle-1.png", "Sprites/Enemies/Shadow/idle-2.png", "Sprites/Enemies/Shadow/idle-3.png", "Sprites/Enemies/Shadow/idle-4.png"]
        self._current_frame = 0
        self.set_actions(
            [
                EnemyAction("damage", get_stat(Shadow.DAMAGE, self.battle_index) , 3),
                EnemyAction("shield", get_stat(Shadow.SHIELD_AMOUNT, self.battle_index), 2)
            ]
        )

    def update(self):
        super().update()
        self._current_frame += 0.015
        if self._current_frame >= len(self._animation_list):
            self._current_frame = 0
        self.image = self._animation_list[int(self._current_frame)]
        self.image = pygame.transform.flip(self._image, True, False)
        self.scale = (4, 4)
