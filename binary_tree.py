class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            if not self.search(value):
                self._insert(self.root, value)
            else:
                raise ValueError(f"O valor {value} já existe na árvore!")

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def search(self, value):
        node = self._search(self.root, value)
        return node is not None

    def _search(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def in_order_traversal(self):
        result = []
        self._in_order_traversal(self.root, result)
        return sorted(result)  # Garante que a lista retornada está ordenada

    def _in_order_traversal(self, node, result):
        if node is not None:
            self._in_order_traversal(node.left, result)
            result.append(node.value)
            self._in_order_traversal(node.right, result)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def clear(self):
        self.root = None  # Limpa a árvore
