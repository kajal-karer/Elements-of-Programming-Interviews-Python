import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
import operator

Interval = collections.namedtuple('Interval', ('left', 'right'))


def find_minimum_visits(intervals):
    intervals.sort(key=operator.attrgetter('right'))
    num_visit = 0
    last_interval_visit = float('-inf')
    for interval in intervals:
        if interval.left > last_interval_visit:
            last_interval_visit = interval.right
            num_visit += 1
    return num_visit


@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_points_covering_intervals.py",
                                       'minimum_points_covering_intervals.tsv',
                                       find_minimum_visits_wrapper))
