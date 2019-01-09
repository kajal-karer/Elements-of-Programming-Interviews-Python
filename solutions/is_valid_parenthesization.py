from test_framework import generic_test


def is_well_formed(s):
    stack, lookup = [], {'(': ')', '{': '}', '[': ']'}
    for par in s:
        if par in lookup:
            stack.append(par)
        elif len(stack) == 0 or lookup[stack.pop()] != par:
            return False
    return len(stack) == 0

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
