from Scene import Scene
import globals
from Text import Text


def create_energy_text():
    txt = Text(
        text="Energy: 0/0",
        position=(150, globals.HEIGHT - 200),
        font_size=20,
        color=(255, 255, 0),
        font_name="Fonts/Minecraft.ttf"
    )
    return txt


class BattleScene(Scene):
    ENEMY_POSITIONS = ((globals.WIDTH // 10 * 6, globals.HEIGHT // 10 * 6 ), (globals.WIDTH // 10 * 6, globals.HEIGHT // 10 * 2), (globals.WIDTH // 20 * 17, globals.HEIGHT // 10 * 4))
    def __init__(self, player, enemies: list):
        super().__init__()
        self.energy_text: Text = create_energy_text()
        self.update_energy_text()
        self.add_object(self.energy_text)
        self.add_object(player)
        self.enemies = enemies
        globals.player.position = (globals.WIDTH // 4, globals.HEIGHT // 2)
        globals.player.create_hp_bar()
        if len(enemies) > 3:
            raise ValueError("Maximum of 3 enemies allowed")
        for i, enemy in enumerate(enemies):
            enemy.position = self.ENEMY_POSITIONS[i]
            self.add_object(enemy)
            enemy.create_hp_bar()

    def render(self, screen):
        super().render(screen)
        if globals.deck is not None:
            globals.deck.render(screen)

    def update_energy_text(self):
        self.energy_text.text = f"Energy: {globals.player.energy}/{globals.player.max_energy}"