# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node
# of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
# You can return any of them.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root, val: int):
        new_node = TreeNode(val)
        if root is None:
            root = new_node
            return root
        else:
            curr = root
            while True:
                if val < curr.val:
                    if curr.left is None:
                        curr.left = new_node
                        return root
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = new_node
                        return root
                    else:
                        curr = curr.right

# Recursive version
    def insert_recursive(self, root, val: int):
        if root is None:
            root = TreeNode(val)

        if val < root.val:
            root.left = self.insert_recursive(root.left, val)
        elif val > root.val:
            root.right = self.insert_recursive(root.right, val)

        return root