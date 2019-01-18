from test_framework import generic_test


def preorder_traversal(tree):
    stack, res = [tree], []
    while stack:
        curr = stack.pop()
        if curr:
            res.append(curr.data)
            stack.extend([curr.right, curr.left])
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_preorder.py", 'tree_preorder.tsv',
                                       preorder_traversal))
