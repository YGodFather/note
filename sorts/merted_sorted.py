# -*- coding: utf-8 -*-#
# Name:         merted_sorted
# Author:       YangRui
# Date:         2020/1/15

def merge_sort(collection):
    def merge(left, right):
        """merge left and right
        :param left: left collection
        :param right: right collection
        :return: merge result
        """
        result = []
        while left and right:
            result.append((left if left[0] <= right[0] else right).pop(0))
        return result + left + right

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))
