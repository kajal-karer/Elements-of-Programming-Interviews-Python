import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import (binary_tree_height,
                                              generate_inorder)
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

class TreeNode:
    def __init__(self, x):
        self.left, self.right = None, None
        self.data = x

def build_min_height_bst_from_sorted_array(A):
    return build_min_height_bst_from_sorted_array_recurr(A, 0, len(A)-1)

def build_min_height_bst_from_sorted_array_recurr(A, begin, end):
    if begin > end:
        return None
    mid = (begin+end) // 2
    node = TreeNode(A[mid])
    node.left = build_min_height_bst_from_sorted_array_recurr(A, begin, mid-1)
    node.right = build_min_height_bst_from_sorted_array_recurr(A, mid+1, end)
    return node

@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(
        functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure("Result binary tree mismatches input array")
    return binary_tree_height(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "bst_from_sorted_array.py", 'bst_from_sorted_array.tsv',
            build_min_height_bst_from_sorted_array_wrapper))
