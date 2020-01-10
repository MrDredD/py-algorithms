# python3
import sys

"""
O(n*log(n))
"""


def compute_min_refills(distance, tank, stops, n):
    stops.append(distance)
    stops = [0] + stops
    prev_stop, counter = 0, 0
    n += 1
    i = 0
    while True:
        j = i + 1
        max_dist = 0
        if stops[i] == distance:
            break
        while j <= n:
            if (stops[j] - stops[i] <= tank) and (stops[j] - stops[i] > max_dist):
                max_dist = stops[j] - stops[i]
            elif stops[j] - stops[i] > tank and max_dist != 0:
                counter += 1
                break
            elif stops[j] - stops[i] > tank and max_dist == 0:
                return -1
            j += 1

        i = j - 1

    return counter


if __name__ == '__main__':
    d, m, n, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops, n))
