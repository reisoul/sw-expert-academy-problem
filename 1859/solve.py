# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc

import sys
from pathlib import Path

sys.stdin = open(Path(__file__).parent / "input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    # N = int(input())
    # price_list = list(map(int, input().split()))
    # len_price_list = len(price_list)

    # 시간초과
    # benefit = 0
    # for idx_i, i in enumerate(price_list):
    #     if idx_i + 1 == len_price_list:
    #         break

    #     max_value = i
    #     for idx_j in range(idx_i + 1, len_price_list):
    #         if max_value < price_list[idx_j]:
    #             max_value = price_list[idx_j]

    #     benefit += max_value - i

    # 뒤집어서
    N = int(input())
    price_list = list(map(int, input().split()))[::-1]
    benefit = 0
    max_value = price_list[0]

    # 2 1 3 1 1
    for idx_i in range(N - 1):
        idx_j = idx_i + 1

        if max_value < price_list[idx_i]:
            max_value = price_list[idx_i]

        if max_value > price_list[idx_j]:
            benefit += max_value - price_list[idx_j]

    print(f"#{test_case} {benefit}")
