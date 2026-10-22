
from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)

  