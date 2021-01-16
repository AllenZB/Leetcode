from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i

        def recur(in_start, in_end, pre_start, pre_end):
            if in_start <= in_end:
                root = TreeNode(preorder[pre_start])
                index = dic[root.val]
                index_delta = index - in_start
                root.left = recur(in_start, index - 1, pre_start + 1, pre_start + index_delta)
                root.right = recur(index + 1, in_end, pre_start + index_delta + 1, pre_end)
                return root
            else:
                return None

        return recur(0, len(inorder) - 1, 0, len(preorder) - 1)
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print(Solution().buildTree(preorder,inorder).val)
