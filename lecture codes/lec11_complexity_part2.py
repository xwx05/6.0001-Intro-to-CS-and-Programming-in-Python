# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:13:13 2016

@author: ericgrimson
"""


def bisect_search2(L, e):
    # 使用helper函数，不用每次copy整个列表并切割为1/2，而是将原列表上要查找的范围[low, high]cut为1/2
    def bisect_search_helper(L, e, low, high):
        print('low: ' + str(low) + '; high: ' + str(high))  # added to visualize
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:  # nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)


testList = []
for i in range(100):
    testList.append(i)

print(bisect_search2(testList, 76))

"""
概念：
1、要生成1～n的的全部子集
2、假设可以生成1～n-1的全部子集
3、则2中生成的1～n-1的全部子集 + 1～n-1的全部子集中的每一个加上n，即为1～n的的全部子集
"""

"""
原始列表 L = [1, 2, 3, 4]，每次递归调用时，传入的列表依次变为 [1, 2, 3]，[1,2]，[1]，[]，每次调用函数都会有自己的域
最内层调用时，L = []，第一次返回了[[]]结果存储在smaller变量中，返回了上一层调用，其所处的函数域里L = [1]，smaller = [[]]
然后执行extra = L[-1:]就会等于 [1]，这一层调用返回的结果为[[], [1]]，返回上一层调用，其所处的函数域里L = [1，2]，依此类推
"""

def genSubsets(L):
    if len(L) == 0:
        # return的结果存储在smaller变量中，因为之后genSubset()函数的结果赋值给了smaller变量
        return [[]]  # list of empty list，单独写出空集的情况
    smaller = genSubsets(L[:-1])  # 递归地调用 genSubsets(L[:-1])，这会生成不包含最后一个元素的所有子集，将结果存储在 smaller 中
    extra = L[-1:]  # 创建一个只包含输入列表最后一个元素的列表 extra
    new = []
    # 遍历 smaller 中的每个子集 small，通过将 extra 中的元素添加到 small 中来创建新的子集，并将这些新子集存储在 new 列表中
    # 最后，返回 smaller（不包含最后一个元素的子集）和 new（包含最后一个元素的新子集）的组合，这样就得到了输入列表 L 的所有子集
    for small in smaller:
        new.append(small + extra)  # for all smaller solutions, add one with last element
    return smaller + new  # combine those with last element and those without


testSet = [1, 2, 3, 4]
print(genSubsets(testSet))
