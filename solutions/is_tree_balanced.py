from test_framework import generic_test


def is_balanced_binary_tree(root):
    return getHeight(root) >= 0

def getHeight(root):
    if not root:
        return 0
    lheight, rheight = getHeight(root.left), getHeight(root.right)
    if lheight < 0 or rheight < 0 or abs(lheight - rheight) > 1:
        return -1
    return max(rheight, lheight) + 1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
