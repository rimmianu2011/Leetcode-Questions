# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []
        
        def inorder_traversal(root, result):
            if not root:
                return None

            else:
                inorder_traversal(root.left, result)
                result.append(root.val)
                inorder_traversal(root.right, result)
            
        inorder_traversal(root, result)
        return result