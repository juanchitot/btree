from btree import Node
import pytest
#createFromArray()
def test_cero_heigh_create():
    nodeA = Node(10)
    nodeB = Node.createFromArray([10])
    assert nodeA.value == nodeB.value
    assert nodeA.right == nodeB.right
    assert nodeA.left == nodeB.left

def test_complete_tree_create():
    #             20
    #     11              33
    # 9       12      31      34
    node_level_2_0 = Node(9)
    node_level_2_1 = Node(12)
    node_level_2_2 = Node(31)
    node_level_2_3 = Node(34)

    node_level_1_0 = Node(11)
    node_level_1_0.left = node_level_2_0
    node_level_1_0.right = node_level_2_1

    node_level_1_1 = Node(33)
    node_level_1_1.left = node_level_2_2
    node_level_1_1.right = node_level_2_3

    rootA = Node(20)
    rootA.left = node_level_1_0
    rootA.right = node_level_1_1
    #now build tree B
    rootB = Node.createFromArray([20,11,33,9,12,31,34])
    #both should be equals
    assert repr(rootA) == repr(rootB)
    assert rootA.isBtree() == True

#min and max
def test_min_and_max_cero_height_tree():
    node = Node(10)
    assert node.max() == 10
    assert node.min() == 10

def test_min_and_max_full_btree():
    node = Node.createFromArray([20,11,33,9,12,31,34])
    assert node.max() == 34
    assert node.min() == 9

def test_min_and_max_unordered_tree():
    #             34
    #     13              31
    # 9       11      33      20
    node_level_2_0 = Node(9)
    node_level_2_1 = Node(11)
    node_level_2_2 = Node(33)
    node_level_2_3 = Node(20)

    node_level_1_0 = Node(13)
    node_level_1_0.left = node_level_2_0
    node_level_1_0.right = node_level_2_1

    node_level_1_1 = Node(31)
    node_level_1_1.left = node_level_2_2
    node_level_1_1.right = node_level_2_3

    root = Node(34)
    root.left = node_level_1_0
    root.right = node_level_1_1

    assert root.max() == 34
    assert root.min() == 9
    assert root.isBtree() == False

#height()
def test_cero_heigh():
    node = Node(10)
    assert node.height() == 0

def test_only_left_childs_height():
    node = Node(100)
    node.add(75)
    assert node.height() == 1
    node.add(50)
    assert node.height() == 2
    node.add(25)
    assert node.height() == 3

def test_balanced_tree_heigh():
    node = Node.createFromArray([20,11,33,9,12,31,34])
    assert node.height() == 2

def test_unbalanced_tree_heigh():
    node = Node.createFromArray([20,11,33,10])
    assert node.height() == 2

#deepest()
def test_cero_heigh_deepest():
    node = Node(11)
    assert node.deepest() == [(0,11)]

def test_balanced_tree_deepest():
    node = Node.createFromArray([20,11,33,9,12,31,34])
    assert node.deepest() == [(2,9),(2,12),(2,31),(2,34)]


#find()
def test_leaf_node_fail():
    leaf = Node(20)
    with pytest.raises(Exception) as exc_info:
        leaf.find(10)
    assert str(exc_info.value) == "Value 10 not found"

def test_leaf_node_success():
    leaf = Node(20)
    assert type(leaf.find(20)).__name__ == 'Node'

def test_on_full_tree():
    root = Node.createFromArray([20,11,33,9,12,31,34])
    result = root.find(31)
    assert type(result).__name__ == 'Node'
    assert result.value == 31

# remove
def test_remove_leaf():
    #             20
    #     11              33
    # 9       12      31      34
    node = Node.createFromArray([20,11,33,9,12,31,34])
    node = node.remove(34)
    assert node.max() == 33
    assert node.min() == 9
    assert node.isBtree() == True
    assert node.height() == 2
    with pytest.raises(Exception) as exc_info:
        node.find(34)
    assert str(exc_info.value) == "Value 34 not found"

def test_remove_on_full_tree():
    #             20
    #     11              33
    # 9       12      31      34
    node = Node.createFromArray([20,11,33,9,12,31,34])
    node = node.remove(20)
    #
    #     11
    # 9        12
    #                 33
    #             31     34
    assert node.max() == 34
    assert node.min() == 9
    assert node.isBtree() == True
    assert node.height() == 3
    with pytest.raises(Exception) as exc_info:
        node.find(20)
    assert str(exc_info.value) == "Value 20 not found"
