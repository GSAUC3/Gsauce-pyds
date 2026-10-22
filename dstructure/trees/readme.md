```
binary_tree/
│
├── binary_tree/
│   │
│   ├── __init__.py
│   │
│   ├── node.py
│   ├── binary_tree.py
│   ├── builder.py
│   ├── serializer.py
│   ├── pretty_print.py
│   ├── exceptions.py
│   ├── utils.py
│   │
│   ├── traversals/
│   │   ├── __init__.py
│   │   ├── preorder.py
│   │   ├── inorder.py
│   │   ├── postorder.py
│   │   ├── level_order.py
│   │   ├── zigzag.py
│   │   └── boundary.py
│   │
│   ├── algorithms/
│   │   ├── __init__.py
│   │   ├── height.py
│   │   ├── depth.py
│   │   ├── diameter.py
│   │   ├── width.py
│   │   ├── balanced.py
│   │   ├── mirror.py
│   │   ├── symmetry.py
│   │   ├── paths.py
│   │   ├── lca.py
│   │   ├── sum.py
│   │   ├── max.py
│   │   ├── min.py
│   │   ├── count.py
│   │   └── views.py
│   │
│   ├── protocols/
│   │   ├── __init__.py
│   │   ├── iterable.py
│   │   ├── comparable.py
│   │   └── printable.py
│   │
│   └── visualizer/
│       ├── ascii.py
│       ├── unicode.py
│       └── graphviz.py
│
├── tests/
│   ├── test_node.py
│   ├── test_tree.py
│   ├── test_traversals.py
│   ├── test_algorithms.py
│   ├── test_protocols.py
│   └── test_serializer.py
│
├── examples/
│   ├── build_tree.py
│   ├── traversals.py
│   ├── algorithms.py
│   ├── serialization.py
│   └── visualization.py
│
├── docs/
│   ├── node.md
│   ├── binary_tree.md
│   ├── traversals.md
│   ├── algorithms.md
│   └── complexity.md
│
├── README.md
├── requirements.txt
└── pyproject.toml
```

---

# `Node`

```
Node
│
├── data
├── left
├── right
│
├── is_leaf()
├── degree()
├── has_left()
├── has_right()
├── children()
│
├── __repr__()
├── __str__()
├── __eq__()
└── __hash__()
```

---

# `BinaryTree`

```
BinaryTree
│
├── root
├── size
│
├── Construction
│   ├── insert()
│   ├── clear()
│   ├── copy()
│   ├── clone()
│   ├── from_list()
│   ├── from_preorder()
│   ├── from_inorder()
│   ├── from_postorder()
│   └── from_levelorder()
│
├── Traversals
│   ├── preorder()
│   ├── inorder()
│   ├── postorder()
│   ├── level_order()
│   ├── zigzag()
│   ├── boundary()
│   ├── left_view()
│   ├── right_view()
│   ├── top_view()
│   └── bottom_view()
│
├── Statistics
│   ├── size()
│   ├── height()
│   ├── depth()
│   ├── width()
│   ├── diameter()
│   ├── leaf_count()
│   ├── internal_count()
│   ├── degree_one_count()
│   ├── degree_two_count()
│   ├── maximum()
│   ├── minimum()
│   ├── sum()
│   └── average()
│
├── Searching
│   ├── contains()
│   ├── find()
│   └── path_to()
│
├── Transformations
│   ├── mirror()
│   ├── invert()
│   ├── reverse()
│   ├── balance()
│   └── flatten()
│
├── Validation
│   ├── is_empty()
│   ├── is_balanced()
│   ├── is_complete()
│   ├── is_full()
│   ├── is_perfect()
│   ├── is_degenerate()
│   └── is_symmetric()
│
├── Serialization
│   ├── to_list()
│   ├── to_dict()
│   ├── to_json()
│   ├── save()
│   └── load()
│
├── Visualization
│   ├── print()
│   ├── pretty()
│   ├── ascii()
│   ├── unicode()
│   └── graphviz()
│
└── Python Protocols
    ├── __len__()
    ├── __iter__()
    ├── __contains__()
    ├── __repr__()
    ├── __str__()
    ├── __bool__()
    ├── __eq__()
    ├── __copy__()
    ├── __deepcopy__()
    ├── __getitem__()
    └── __reversed__()
```

---

# Traversal Hierarchy

```
Traversal
│
├── Recursive
│   ├── preorder
│   ├── inorder
│   ├── postorder
│   └── level_order
│
├── Iterative
│   ├── preorder
│   ├── inorder
│   ├── postorder
│   └── level_order
│
└── Generator Versions
    ├── preorder_iter()
    ├── inorder_iter()
    ├── postorder_iter()
    └── level_order_iter()
```

---

# Helper (Private) Methods

```
_build()

_clone()

_insert()

_height()

_depth()

_diameter()

_width()

_contains()

_find()

_path()

_sum()

_maximum()

_minimum()

_leaf_count()

_internal_count()

_degree_one()

_degree_two()

_balance()

_mirror()

_flatten()

_validate()

_pretty()

_ascii()

_graphviz()

_serialize()

_deserialize()
```

---

# Utility Classes

```
Queue

Stack

TreeBuilder

TreeSerializer

TreePrinter

GraphvizExporter
```

---

# Exception Hierarchy

```
TreeError
│
├── EmptyTreeError
├── InvalidTraversalError
├── InvalidTreeError
├── NodeNotFoundError
└── SerializationError
```

---

# Python Protocol Support

```
len(tree)

bool(tree)

tree == other

x in tree

iter(tree)

reversed(tree)

print(tree)

repr(tree)

copy.copy(tree)

copy.deepcopy(tree)
```

---

# Future Expansion

```
BinaryTree
        │
        ├──────────────┐
        │              │
        ▼              ▼
BinarySearchTree     ExpressionTree
        │              │
        ▼              ▼
      AVLTree      HuffmanTree
        │
        ▼
   RedBlackTree
        │
        ▼
      BTree
        │
        ▼
      B+Tree
```

---

# Suggested Development Order

```
Phase 1
────────
☐ Node
☐ BinaryTree
☐ Pretty Print

Phase 2
────────
☐ Recursive Traversals
☐ Iterative Traversals
☐ Generator Traversals

Phase 3
────────
☐ Height
☐ Size
☐ Sum
☐ Maximum
☐ Minimum
☐ Counts

Phase 4
────────
☐ Diameter
☐ Width
☐ Balance
☐ Symmetry
☐ Views

Phase 5
────────
☐ Serialization
☐ Builder
☐ File IO

Phase 6
────────
☐ Python Protocols
☐ Visualization
☐ Testing
☐ Documentation

Phase 7
────────
☐ BinarySearchTree

Phase 8
────────
☐ AVL Tree

Phase 9
────────
☐ Red Black Tree

Phase 10
────────
☐ B Tree
☐ B+ Tree
☐ Trie
☐ Segment Tree
☐ Fenwick Tree
```
