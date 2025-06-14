from Button import Button
from Enemy import Enemy
from Scene import Scene
import globals
from Text import Text
from fix_png import fix_png_profiles


def create_energy_text():
    txt = Text(
        text="Energy: 0/0",
        position=(150, globals.HEIGHT - 200),
        font_size=20,
        color=(255, 255, 0),
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
        self.enemies: list[Enemy] = enemies
        globals.player.position = (globals.WIDTH // 4, globals.HEIGHT // 2)
        if len(enemies) > 3:
            raise ValueError("Maximum of 3 enemies allowed")
        for i, enemy in enumerate(enemies):
            enemy.position = self.ENEMY_POSITIONS[i]
            self.add_object(enemy)
            
        # end turn button
        self.end_turn_button = Button(
            position=(globals.WIDTH - 200, globals.HEIGHT - 100),
            width=200,
            height=50,
            text="End turn",
            on_click=self.end_player_turn
        )
        self.add_object(self.end_turn_button)
        self.start_player_turn()

    def render(self, screen):
        super().render(screen)
        if globals.deck is not None:
            globals.deck.render(screen)

    def update_energy_text(self):
        self.energy_text.text = f"Energy: {globals.player.energy}/{globals.player.max_energy}"
    
    def end_player_turn(self):
        for e in self.enemies:
            e.perform_action()
        self.start_player_turn()
    
    def start_player_turn(self):
        for e in self.enemies:
            e.request_action()
        globals.player.energy = globals.player.max_energy
        self.update_energy_text()
        
    def check_enemies_dead(self):
        for e in self.enemies:
            if not e.dead:
                return
        raise RuntimeError("Implement new scene")