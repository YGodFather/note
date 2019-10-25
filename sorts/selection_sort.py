# coding:utf-8

# 选择排序


def swap(lyst, i, j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


def selection_sort(lyst):
    temp_list = list(lyst)
    i = 0
    while i < len(temp_list) - 1:
        min_idx = i
        j = i + 1
        while j < len(temp_list):
            if temp_list[j] < temp_list[min_idx]:
                min_idx = j
            j += 1
        if min_idx != i:
            swap(temp_list, min_idx, i)
        i += 1
    return temp_list


if __name__ == '__main__':
    not_sort = [8, 5, 0, 4, 3]

    print(selection_sort(not_sort))
