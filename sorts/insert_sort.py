# -*- coding: utf-8 -*-#
# Name:         insert_sort
# Author:       YangRui
# Date:         2019/10/24


"""
1、左面的数据为已排序的数组
2、从右面数组中取值出来，于左面的数组值一一相比较

"""

def insert_sort(lyst):
    """
    :param lyst:list
    :return: sorted list
    """
    tmp_list = list(lyst)
    i = 1
    while i < len(tmp_list):
        item_to_insert = tmp_list[i]
        j = i - 1
        while j >= 0:
            if item_to_insert < tmp_list[j]:
                tmp_list[j + 1] = tmp_list[j]
                j -= 1
            else:
                break
        tmp_list[j + 1] = item_to_insert
        i += 1

    return tmp_list


if __name__ == '__main__':
    test_array = [0, 9, 6, 8, 0]
    print(insert_sort(test_array))