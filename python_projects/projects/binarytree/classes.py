from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value, self.root)

    def _insert_recursive(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(value, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(value, current_node.right)

    def search(self, value):
        return self._search_recursive(value, self.root)

    def _search_recursive(self, value, current_node):
        if current_node is None or current_node.value == value:
            return current_node
        elif value < current_node.value:
            return self._search_recursive(value, current_node.left)
        else:
            return self._search_recursive(value, current_node.right)

    def breadth_first_search(self):
        if self.root is None:
            return []

        result = []
        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()
            result.append(node.value)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return result
    
    def depth_first_search(self):
        if self.root is None:
            return []

        result = []
        stack = []
        stack.append(self.root)

        while stack:
            node = stack.pop()
            result.append(node.value)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return result

    def get_tree_level(self):
        if self.root is None:
            return 0

        level = 0
        queue = deque()
        queue.append(self.root)

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level += 1

        return level
    
    def create_new_tree(self, leaf_value):
        leaf = self.search(leaf_value)
        if leaf is None:
            return None

        new_tree = BinaryTree()
        new_tree.root = leaf
        return new_tree
    
    def display_tree(self):
        def display_tree_helper(node, level=0):
            if node is None:
                return

            display_tree_helper(node.right, level + 1)
            print("    " * level + str(node.value))
            display_tree_helper(node.left, level + 1)

        display_tree_helper(self.root)