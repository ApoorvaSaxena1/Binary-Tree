# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    @staticmethod
    def parseTree(node,level,arr):
        if len(arr)<level:
            arr.append([node.val])
        else:
            arr[level-1].append(node.val)
            
        if node.left!=None:
            arr=Solution.parseTree(node.left,level+1,arr)
        if node.right!=None:
            arr=Solution.parseTree(node.right,level+1,arr)
            
        return arr
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        arr=Solution.parseTree(root,1,[])
        return arr
