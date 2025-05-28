from Scene import Scene
import globals

class BattleScene(Scene):
    ENEMY_POSITIONS = ((globals.WIDTH // 10 * 6, globals.HEIGHT // 10 * 6 ), (globals.WIDTH // 10 * 6, globals.HEIGHT // 10 * 2), (globals.WIDTH // 20 * 17, globals.HEIGHT // 10 * 4))
    def __init__(self, player, enemies: list):
        super().__init__()
        self.add_object(player)
        player.position = (globals.WIDTH // 4, globals.HEIGHT // 2)
        if len(enemies) > 3:
            raise ValueError("Maximum of 3 enemies allowed")
        for i, enemy in enumerate(enemies):
            enemy.position = self.ENEMY_POSITIONS[i]
            self.add_object(enemy)