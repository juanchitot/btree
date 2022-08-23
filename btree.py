#!/usr/bin/env python
import argparse

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        """Flattened representation of the tree"""
        return "(%s, %s, %s)" % (self.left, self.value, self.right)

    def add(self, value):
        """Adds a value to the tree in a ordered place"""
        if value < self.value:
            if self.left is not None:
                self.left.add(value)
            else:
                self.left = Node(value)
        if value > self.value:
            if self.right is not None:
                self.right.add(value)
            else:
                self.right = Node(value)


    def remove(self, value):
        """ Removes 'value' from the tree and reorder the nodes"""

        if self.value== value :
            if self.left is None and self.right is None:
                return None
            if self.left is not None:
                return self.left.attach(self.right)
            else:
                return self.right
        elif self.value < value:
            if self.right is not None:
                self.right = self.right.remove(value)
            return self

        else: # self.value > value
            if self.left is not None:
                self.left = self.left.remove(value)
            return self

    def isBtree(self):
        """Checks if the tree fulfills the conditions to be a Btree"""
        if self.left is not None and self.right is not None:
            return self.left.max() < self.value and self.right.min() > self.value
        elif self.left is None :
            return self.right is None or self.right.min() > self.value
        else: # self.right is None :
            return self.left.max() < self.value

    def max(self):
        """Gets the max value of the tree without taking account if is a Btree"""
        return max(self.value,self.left.max() if self.left is not None else self.value ,self.right.max() if self.right is not None else self.value)

    def min(self):
        """Gets the min value of the tree without taking account if is a Btree"""
        return min(self.value, self.left.min() if self.left is not None else self.value, self.right.min() if self.right is not None else self.value)

    def attach(self, node):
        """Attaches a node to another in a ordered way.
        The passed node must to be a Btree.
        Auxiliary function"""
        if self.value == node.value or not node.isBtree():
            raise ValueException("The node can't be attached")

        if self.value < node.value:
            if self.right is None:
                self.right = node
            else:
                print("hago el attach en %s" % self.right)
                self.right = self.right.attach(node)
            return self

        elif self.value > node.value:
            if self.left is None:
                self.left = node
            else:
                self.left = self.left.attach(node)
            return self

    def height(self):
        l_height = 0
        r_height = 0
        if self.left is not None:
            l_height = 1 + self.left.height()
        if self.right is not None:
            r_height = 1 + self.right.height()
        return max( l_height, r_height)

    def deepest(self):
        deepests = [(0,self.value)]
        if self.left is not None:
            deepests += [ (child[0]+1,child[1]) for child in self.left.deepest() ]

        if self.right is not None:
            deepests += [ (child[0]+1,child[1]) for child in self.right.deepest() ]

        max_depth_tuple = max(deepests, key=lambda x: x[0])
        return list(filter(lambda y: y[0]==max_depth_tuple[0],deepests))

    def find(self, value):
        if self.value == value:
            return self
        if self.value > value and self.left is not None:
            return self.left.find(value)
        if self.value < value and self.right is not None:
            return self.right.find(value)
        raise LookupError("Value %s not found" % value)

    @classmethod
    def createFromArray(cls, vector):
        """ Create a Btree from an unordered array """
        value = vector.pop(0)
        node = Node(value)
        for i in vector:
            node.add(i)
        return node


def main():
    parser = argparse.ArgumentParser(description='Btree search deepest value')
    parser.add_argument('--tree',nargs='+',metavar='INTEGER',type=int,required=True, help='Enter the tree elements with spaces')
    parsed=parser.parse_args()
    if parsed.tree is None:
        parser.print_help()
    else:
        tree_list = parsed.tree
        # validate_tree(tree_list)
        root = Node.createFromArray(tree_list)
        print("Tree with height %d " % root.height())
        print("Deepest values  %s " % root.deepest())


if __name__ == '__main__':
    main()
else:
    pass
