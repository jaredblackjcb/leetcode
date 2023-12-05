from collections import deque
from typing import Optional, List

from main import TreeNode


class TreeToolbox:
    class Node:
        def __init__(self, val=None, children=None):
            self.val = val
            self.children = children

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    ########################### DFS ####################################
    # Postorder Traversal
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Tracking answer in a stack seems cleaner than using yield and yield from to create a recursive generator
        answer = []

        def postorder(node):
            if not node:
                return None
            postorder(node.left)
            postorder(node.right)
            answer.append(node.val)

        postorder(root)
        return answer

    # Binary Tree max depth/height
    def maxDepthBinary(self, root: TreeNode):
        if root is None:
            return 0
        maxLeft = self.maxDepth(root.left)
        maxRight = self.maxDepthBinary(root.right)
        return max(maxLeft, maxRight) + 1

    def minDepthBinary(self, root: TreeNode):
        if root is None:
            # Found the leaf node
            return 0
        if not root.left: # Then the min leaf must be on the right
            return 1 + self.minDepthBinary(root.right)
        if not root.right: # Then the min leaf must be on the left
            return 1 + self.minDepthBinary(root.left)
        return 1 + min(self.minDepthBinary(root.left), self.maxDepthBinary(root.right))

    # Max depth DFS on a n-ary tree with recursion
    def maxDepthNary(self, root: 'Node') -> int:
        # Return 0 if no root node
        if not root:
            return 0
        elif not root.children:
            return 1
        else:
            height = [self.maxDepth(c) for c in root.children]
            return max(height) + 1

    # Max depth DFS without recursion using a stack
    # Time: O(N)
    # Space: O(N)
    def maxDepthNonRecursive(self, root: Node) -> int:
        # Return 0 if no root node
        if not root:
            return 0

        # Maintain a stack of the remaining nodes to traverse
        stack = [(root, 1)]
        maxDepth = 0

        # Iterate through the stack while keeping track of the depth of each node
        while stack:
            root, currentDepth = stack.pop()
            maxDepth = max(maxDepth, currentDepth)
            for c in root.children:
                stack.append((c, currentDepth + 1))

        return maxDepth

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left, right):
            if not left and not right:
                return True
            # Return false if only one of them is None, or if the values don't match
            if (not left or not right) or (left.val != right.val): # At this point we know they are not both None, so it is sufficient to check if one is None
                return False
            # Both sides of the tree must be mirrors
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)

        # Handle null input
        if not root:
            return None
        return isMirror(root.left, root.right)


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p or not q) or (p.val != q.val):
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # Array is already sorted in asc order. If it wasn't, I would have to sort it first
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(leftIndex, rightIndex):
            if leftIndex > rightIndex:
                return None
            # The root is the right middle num from nums
            rootIndex = (leftIndex + rightIndex) // 2

            # preorder traverse: node -> left -> right
            root = TreeNode(nums[rootIndex])
            # Left half of the tree, not including the root index
            root.left = helper(leftIndex, rootIndex - 1)
            # Right half of the tree, not including root index
            root.right = helper(rootIndex + 1, rightIndex)
            return root

        return helper(0, len(nums) - 1)

    def bfs(self, root: TreeNode):
        nextLevel = deque([root])

        while nextLevel:
            currLevel = nextLevel
            nextLevel = deque()

            for n in currLevel:
                if n.left:
                    nextLevel.append(n.left)
                if n.right:
                    nextLevel.append(n.right)