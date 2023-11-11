from classes import BinaryTree
from random import randint


def random_numbers(values_size):
    return [randint(1, 100) for _ in range(values_size)]


def create_level_4_tree(tree = BinaryTree()):
    nums = random_numbers(14)
    for i in nums:
        tree.add(i)
        if tree.get_tree_level() == 4:
            return tree


tree = BinaryTree()
tree.add(5)
tree.add(3)
tree.add(7)
tree.add(1)
tree.add(4)
tree.add(6)
tree.add(9)
tree.display_tree()
