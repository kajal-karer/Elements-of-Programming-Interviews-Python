from test_framework import generic_test

import operator
def evaluate(tokens):
    lookup = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = []
    delimiter = ','
    for token in tokens.split(delimiter):
        if token not in lookup:
            stack.append(int(token))
        else:
            y, x = stack.pop(), stack.pop()
            stack.append(int(lookup[token](x, y)))
    return stack[-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
