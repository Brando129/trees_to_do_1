
# Node Class
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Create an add(val) method on the BST object to add new value to
    # the tree. This entails creating a BTNode with this value and connecting
    # it at the appropriate place in the tree. Unless specified otherwise, BSTs
    # can contain duplicate values.

    # Add
    def add(self,value):
        if(self.root):
            runner = self.root
            while(runner):
                if(value>runner.value):
                    if(runner.right):
                        runner = runner.right
                    else:
                        runner.right = Node(value)
                        return self
                else:
                    if(runner.left):
                        runner = runner.left
                    else:
                        runner.left = Node(value)
                        return self
        self.root = Node(value)
        return self


    # Create a contains(val) method on BST that returns whether the tree contains a
    # given value. Take advantage of the BST structure to make this a much more
    # rapid operation than SList.contains() would be.

    # Contain
    def contains(self, value):
        runner = self.root
        while runner:
            if value == runner.value:
                return True

            if value < runner.value:
                if (not runner.left):
                    return False
                runner = runner.left
            else:
                if (not runner.right):
                    return False
                runner = runner.right
        return False

    # Create a min() method on the BST class that returns the smallest value found in the BST.
    # Minimum
    def min(self):
        runner = self.root
        min = self.root.value
        while runner.left:
            if runner.left.value < min:
                min = runner.left.value
            runner = runner.left

        return min

    # Create a max() BST method that returns the largest value contained in the binary search tree.
    # Max
    def max(self):
        runner = self.root
        max = self.root.value
        while(runner.right):
            if(runner.right.value > max):
                max = runner.right.value

            runner = runner.right

        return max

    # Write a size() method that returns the number of nodes (values) contained in the tree.
    # Size
    def size(self):
        if self.root == None:
            return 0

        def sizeHelp(runner):
            if (not runner):
                return 0
            return 1 + sizeHelp(runner.left) + sizeHelp(runner.right)
        return sizeHelp(self.root)

    # Empty
    # Create an isEmpty() method to return whether the BST is empty (whether it contains no values).
    def isEmpty(self):
        if self.root:
            return False