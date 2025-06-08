from typing import Protocol

class Clickable(Protocol):
    def click(self) -> None: ...
