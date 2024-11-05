# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 11:27:54 2016

@author: ericgrimson
"""

"""
when e is first	element	in	the	list -> BEST CASE	
when e is not in list -> WORST CASE	
when look through about half of the	elements in	list -> AVERAGE	CASE
"""
# worst	case: maximum running time over	all	possible inputs	of a given size len(L)
def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found


testList = [1, 3, 4, 5, 9, 18, 27]

# linear search on sorted list
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:  # 找到一个大于e的元素后，停止搜索
            return False
    return False

# O(len(L1)*len(L2)), WORST CASE: when L1 and L2 same length, none of elements of L1 in	L2, O(len(L1)^2)
def isSubset(L1, L2):
    for e1 in L1:  # outer loop executed len(L1) times
        matched = False
        for e2 in L2:  # each iteration	will execute inner loop	up to len(L2) times
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True


testSet = [1, 2, 3, 4, 5]
testSet1 = [1, 5, 3]
testSet2 = [1, 6]


def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not (e in res):
            res.append(e)
    return res
