# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 09:21:39 2016

@author: ericgrimson
"""

# 比较连续的元素对，O(n^2)
def bubble_sort(L):
    swap = False
    while not swap:  # 最大元素最差情况会从头交换到尾，所以最多会有len(L)-1 passes -> O(len(L))
        print('bubble sort: ' + str(L))
        swap = True
        for j in range(1, len(L)):  # len(L)-1 comparisons -> O(len(L))
            if L[j - 1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j - 1]
                L[j - 1] = temp


testList = [1, 3, 5, 7, 2, 6, 25, 18, 13]

print('')
print(bubble_sort(testList))
print(testList)

"""
given prefix of list L[0:i]	and	suffix L[i+1:len(L)],
prefix is sorted and no	element	in prefix is larger than smallest element in suffix	
1. prefix empty, suffix	whole list
2. move	minimum	element	from suffix to end of prefix.
3. when	exit, prefix is	entire list, suffix	empty, so sorted	
"""
def selection_sort(L):  # O(n^2)
    suffixSt = 0
    while suffixSt != len(L):  # len(L) times -> O(len(L))
        print('selection sort: ' + str(L))
        # 前suffixSt个元素已经排序，下一轮在排除前suffixSt个元素的列表里找最小值
        for i in range(suffixSt, len(L)):  # len(L)-suffixSt times -> O(len(L))
            if L[i] < L[suffixSt]:  # suffixSt等于0时，在列表里找比L[suffixSt]小的元素，如果有则把其换到L[0]位置
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1


testList = [1, 3, 5, 7, 2, 6, 25, 18, 13]

print('')
print(selection_sort(testList))
print(testList)

# 对两个sublist来说都只遍历了一次 -> O(n)
def merge(left, right):
    result = []  # O(len(left) + len(right)) copied	elements
    i, j = 0, 0
    # 比较两个sublist里最小的元素，最多	O(len(longer list))	comparisons
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # left list还未遍历完，right list已遍历完
    while (i < len(left)):
        result.append(left[i])
        i += 1
    # right list还未遍历完，left list已遍历完
    while (j < len(right)):
        result.append(right[j])
        j += 1
    print('merge: ' + str(left) + '&' + str(right) + ' to ' + str(result))
    return result

# overall complexity is	O(nlog(n)) where n is len(L)
def merge_sort(L):
    print('merge sort: ' + str(L))
    if len(L) < 2:
        return L[:]  # 列表长度为0或1时，即已排好序
    else:
        middle = len(L) // 2
        # 递归直到sublist长度为0或1
        left = merge_sort(L[:middle])  # dividing list in half -> O(log n)
        right = merge_sort(L[middle:])
        # 对两个已排序的sublist进行合并，合并过程中同时进行排序
        return merge(left, right)  # O(n)


testList = [1, 3, 5, 7, 2, 6, 25, 18, 13]

print('')
print(merge_sort(testList))
