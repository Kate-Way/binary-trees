# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values
# of the nodes you can see ordered from top to bottom.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        answer = {}

        def dfs(node, height):
            if not node:
                return
            if height not in answer:
                answer[height] = node.val

            dfs(node.right, height + 1)
            dfs(node.left, height + 1)

        dfs(root, 0)

        return answer.values()

