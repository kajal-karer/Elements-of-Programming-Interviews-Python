from test_framework import generic_test

class TreeNode:
     def __init__(self, x):
         self.data = x
         self.left = None
         self.right = None

def binary_tree_from_preorder_inorder(preorder, inorder):
        lookup = {}
        for i, num in enumerate(inorder):
            lookup[num] = i
        return buildTreeRecur(preorder, inorder, 0, 0, len(inorder), lookup)

def buildTreeRecur(preorder, inorder, pstart, istart, iend, lookup):
        if istart == iend:
            return None
        node = TreeNode(preorder[pstart])
        inorder_root_index = lookup[preorder[pstart]]
        num_index = inorder_root_index - istart
        node.left = buildTreeRecur(preorder, inorder, pstart + 1, istart, inorder_root_index, lookup)
        node.right = buildTreeRecur(preorder, inorder, pstart + 1 + num_index, inorder_root_index + 1, iend,lookup)
        return node

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
