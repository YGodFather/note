# -*- coding: utf-8 -*-#
# Name:         bubble_sort
# Author:       YangRui
# Date:         2019/10/24


"""
1、将数据一个个的进行比对

[9, 0, 7 ,6 ,4]
"""


def swap(lyst, i, j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


def bubble_sort(lyst):
    tmp_list = list(lyst)
    length = len(tmp_list)
    while length > 1:
        idx = 1
        while idx < length:
            if tmp_list[idx - 1] > tmp_list[idx]:
                swap(tmp_list, idx, idx - 1)
            idx += 1
        length -= 1
    return tmp_list


if __name__ == '__main__':
    test_array = [0, 9, 6, 8, 0]
    print(bubble_sort(test_array))