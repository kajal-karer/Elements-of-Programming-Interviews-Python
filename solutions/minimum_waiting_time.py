from test_framework import generic_test


def minimum_total_waiting_time(service_times):
    service_times.sort()
    total_waiting = 0
    for i, val in enumerate(service_times):
        total_waiting += val * (len(service_times) - (i+1))
    return total_waiting


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_waiting_time.py",
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
