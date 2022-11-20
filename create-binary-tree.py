class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
        else:
            curr = self.root
            while True:
                if val < curr.val:
                    if curr.left is None:
                        curr.left = new_node
                        return
                    else:
                        curr = curr.left

                else:
                    if curr.right is None:
                        curr.right = new_node
                        return
                    else:
                        curr = curr.right

    def lookup(self, val):
        curr = self.root
        if curr is None:
            return
        while curr:
            if curr.val == val:
                return curr
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return

    def remove(self, val):
        curr = self.root
        if curr is None:
            return False
        parent = None
        while curr:
            if val < curr.val:
                parent = curr
                curr = curr.left
            elif val > curr.val:
                parent = curr
                curr = curr.right
            else:
                if curr.right is None:
                    if parent is None:
                        self.root = curr.left
                    elif curr.val < parent.val:
                        parent.left = curr.left
                    else:
                        parent.right = curr.left

                elif curr.right.left is None:
                    if parent is None:
                        self.root = curr.right
                    curr.right.left = curr.left
                    if curr.val < parent.val:
                        parent.left = curr.right
                    elif curr.val > parent.val:
                        parent.right = curr.right

                else:
                    the_parent = curr.right
                    most_left = curr.right.left
                    while most_left:
                        the_parent = most_left
                        most_left = most_left.left
                    the_parent.left = most_left.right
                    most_left.left = curr.left
                    most_left.right = curr.right
                    if parent is None:
                        self.root = most_left
                    if curr.val < parent.val:
                        parent.left = most_left
                    else:
                        parent.right = most_left
                return





