from test_framework import generic_test


def is_binary_tree_bst(root, low=float('-inf'), high=float('inf')):
    if root is None:
        return True
    return low <= root.data and high >= root.data and is_binary_tree_bst(root.left, low, root.data) and is_binary_tree_bst(
        root.right, root.data, high)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
