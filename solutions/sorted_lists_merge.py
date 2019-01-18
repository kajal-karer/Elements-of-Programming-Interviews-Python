from test_framework import generic_test

class ListNode:
    def __init__(self, x):
        self.data = x
        self.next = None

def merge_two_sorted_lists(L1, L2):
    head = tail = ListNode(None)
    while L1 and L2:
        if L1.data < L2.data:
            head.next = L1
            L1 = L1.next
        else:
            head.next = L2
            L2 = L2.next
        head = head.next
    head.next = L1 or L2
    return tail.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
