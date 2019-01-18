from test_framework import generic_test


def inorder_traversal(tree):
    stack, res, done = [], [], 1
    curr = tree
    while done:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            if len(stack):
                curr = stack.pop()
                res.append(curr.data)
                curr = curr.right
            else:
                done = 0
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
