import json
import os
from typing import Type

class SaveManager:
    _instance: 'SaveManager' = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SaveManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, filename="save_data.json"):
        self.filename = filename
        self._load_data()

    @classmethod
    def get_instance(cls: Type["SaveManager"]) -> "SaveManager":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def _load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                try:
                    self.data = json.load(f)
                except json.JSONDecodeError:
                    self.data = {}
        else:
            self.data = {}

    def _save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)

    def save(self, name: str, value: str | int):
        self.data[name] = value
        self._save_data()

    def read(self, name: str):
        return self.data.get(name, None)
    
    def do_something(self):
        print("do something")
