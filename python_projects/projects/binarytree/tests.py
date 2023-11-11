import pytest

from classes import BinaryTree
from main import create_level_4_tree 

@pytest.fixture
def binary_tree():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(1)
    tree.add(4)
    tree.add(6)
    tree.add(9)
    return tree

def test_depth_first_search(binary_tree):
    expected_result = [5, 3, 1, 4, 7, 6, 9]
    assert binary_tree.depth_first_search() == expected_result

def test_breadth_first_search(binary_tree):
    expected_result = [5, 3, 7, 1, 4, 6, 9]
    assert binary_tree.breadth_first_search() == expected_result

def test_get_tree_level(binary_tree):
    assert binary_tree.get_tree_level() == 3

def test_create_new_tree(binary_tree):
    assert binary_tree.create_new_tree(7) == [7, 6, 9]

    new_tree = binary_tree.create_new_tree(4)
    assert new_tree.depth_first_search() == [4]

    new_tree.add(2)
    assert new_tree.depth_first_search() == [4, 2]

    new_tree.add(8)
    assert new_tree.depth_first_search() == [4, 2, 8]

def test_create_level_4_tree():
    assert create_level_4_tree().get_tree_level() == 4
