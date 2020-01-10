# Uses python3
import sys

def lcm_naive(first_num: int, second_num: int):
    if first_num == 0 or second_num == 0:
        return 0
    max_num = first_num if first_num >= second_num else second_num
    common_mult = max_num
    while (common_mult % first_num > 0) or (common_mult % second_num > 0):
        common_mult += max_num
    return common_mult

if __name__ == '__main__':     
    a, b = map(int, input().split())
    print(lcm_naive(a, b))

