from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        value_to_idx = dict()
        for idx, value in enumerate(inorder):
            value_to_idx[value] = idx

        def build(inorder, postorder, in_start, in_end, post_start, post_end):
            if in_start <= in_end:
                root = TreeNode(postorder[post_end])
                in_idx = value_to_idx[root.val]
                in_idx_delta = in_idx - in_start
                root.left = build(inorder, postorder,
                                  in_start, in_idx - 1,
                                  post_start, post_start + in_idx_delta - 1)
                root.right = build(inorder, postorder,
                                   in_start + in_idx_delta + 1, in_end,
                                   post_start + in_idx_delta, post_end - 1)
                return root
            else:
                return None

        return build(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Solution().buildTree(inorder,postorder)