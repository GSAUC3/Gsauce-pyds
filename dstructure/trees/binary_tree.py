from typing import Any

class Node:
    def __init__(self, data: Any) -> None:
        self.parent = None
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return (
            f"Node\n"
            f"├── data   : {self.data}\n"
            f"├── left   : {self.left.data if self.left else None}\n"
            f"├── right  : {self.right.data if self.right else None}\n"
            f"└── parent : {self.parent.data if self.parent else None}"
        )
            

    def __eq__(self, item):
        if not isinstance(item, Node):
            return NotImplemented
        return item.data == item.data

    def __hash__(self):
        pass

    def is_root(self) -> bool:
        return self.parent == None

    def is_leaf(self) -> bool:
        """Return True if the node is a leaf (no children).

        Returns:
            bool: True if the node has no left and no right child, False otherwise.
        """
        return self.left is None and self.right is None

    def degree(self) -> int:... 

    def has_left(self) -> bool:...

    def had_right(self)-> bool: ...

    def descendents(self) -> None:... 

    

    

    