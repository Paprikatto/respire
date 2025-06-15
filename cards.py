from Card import Card

# List of all cards in the game

CARDS_DATA = [
    {
        "actions": {"damage": 10},
        "energy_cost": 2,
        "use_on_player": False,
        "image_path": "Sprites/card-sword.png",
        "sound_path": "Sounds/slice.wav"
    },
    {
        "actions": {"damage": 10},
        "energy_cost": 1,
        "use_on_player": False,
        "image_path": "Sprites/card-sword.png",
        "sound_path": "Sounds/slice.wav"
    },
    {
        "actions": {"damage": 25},
        "energy_cost": 3,
        "use_on_player": False,
        "image_path": "Sprites/card-sword.png",
        "sound_path": "Sounds/slice.wav"
    },
    {
        "actions": {"shield_player": 15},
        "energy_cost": 2,
        "use_on_player": True,
        "image_path": "Sprites/card-shield.png",
        "sound_path": "Sounds/shield.mp3"
    }
]