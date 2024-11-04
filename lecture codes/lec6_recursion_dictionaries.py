# # -*- coding: utf-8 -*-
# """
# Created on Wed Sep 21 11:52:34 2016
#
# @author: WELG
# """
#
#
# #####################################
# # EXAMPLE:  Towers of Hanoi
# # The	story:
# #     3 tall spikes
# #     Stack of 64	different sized	discs –	start on one spike
# #     Need to	move stack to second spike (at which point universe	ends)
# #     Can	only move one disc at a	time, and a	larger disc	can never cover	up a small disc
# #####################################
#
# count=0
# def printMove(fr, to):
#     global count
#     print('move from ' + str(fr) + ' to ' + str(to))
#     # 定义一个全局变量来统计移动次数
#     count += 1
#
# def Towers(n, fr, to, spare):
#
#     # 如果只有一个disc，直接从 from_spike 移到 to_spike，不涉及spare_spike
#     if n == 1:
#         printMove(fr, to)
#     else:
#         # n个disc，把上面n-1个disc先从 from_spike 暂时移到 spare_spike，不涉及to_spike
#         Towers(n - 1, fr, spare, to)
#
#         # 下面最大的一个disc从 from_spike 移到 to_spike，不涉及spare_spike
#         Towers(1, fr, to, spare)
#
#         # 把暂存在 spare_spike 的n-1个disc从暂存的 spare_spike 移到 to_spike，不涉及from_spike
#         Towers(n - 1, spare, to, fr)
#
# print(Towers(4, 'P1', 'P2', 'P3'))
# print(count)
#
# #####################################
# # EXAMPLE:  fibonacci
# #####################################
#
# def fib(x):
#     """assumes x an int >= 0
#        returns Fibonacci of x"""
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return fib(x - 1) + fib(x - 2)
#
#
# #####################################
# # EXAMPLE:  testing for palindromes
# #####################################
#
# def isPalindrome(s):
#     def toChars(s):
#         s = s.lower()
#         ans = ''
#         for c in s:
#             # 只保留英文字符
#             if c in 'abcdefghijklmnopqrstuvwxyz':
#                 ans = ans + c
#         return ans
#
#     def isPal(s):
#         if len(s) <= 1:
#             return True
#         else:
#             return s[0] == s[-1] and isPal(s[1:-1])
#
#     return isPal(toChars(s))


# print(isPalindrome('eve'))
#
# print(isPalindrome('Able was I, ere I saw Elba'))
#
# print(isPalindrome('Is this a palindrome'))
#
# #####################################
# # EXAMPLE: using dictionaries
# #          counting frequencies of words in song lyrics
# #####################################
#
# 创建dict存储出现的单词和对应词频
# def lyrics_to_frequencies(lyrics):
#     myDict = {}
#     for word in lyrics:
#         if word in myDict:
#             myDict[word] += 1
#         else:
#             myDict[word] = 1
#     return myDict
#
#
# she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah',
#                  'yeah', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#                  'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#
#                  'you', 'think', "you've", 'lost', 'your', 'love',
#                  'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
#                  "it's", 'you', "she's", 'thinking', 'of',
#                  'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',
#
#                  'she', 'says', 'she', 'loves', 'you',
#                  'and', 'you', 'know', 'that', "can't", 'be', 'bad',
#                  'yes', 'she', 'loves', 'you',
#                  'and', 'you', 'know', 'you', 'should', 'be', 'glad',
#
#                  'she', 'said', 'you', 'hurt', 'her', 'so',
#                  'she', 'almost', 'lost', 'her', 'mind',
#                  'and', 'now', 'she', 'says', 'she', 'knows',
#                  "you're", 'not', 'the', 'hurting', 'kind',
#
#                  'she', 'says', 'she', 'loves', 'you',
#                  'and', 'you', 'know', 'that', "can't", 'be', 'bad',
#                  'yes', 'she', 'loves', 'you',
#                  'and', 'you', 'know', 'you', 'should', 'be', 'glad',
#
#                  'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#                  'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#                  'with', 'a', 'love', 'like', 'that',
#                  'you', 'know', 'you', 'should', 'be', 'glad',
#
#                  'you', 'know', "it's", 'up', 'to', 'you',
#                  'i', 'think', "it's", 'only', 'fair',
#                  'pride', 'can', 'hurt', 'you', 'too',
#                  'pologize', 'to', 'her',
#
#                  'Because', 'she', 'loves', 'you',
#                  'and', 'you', 'know', 'that', "can't", 'be', 'bad',
#                  'Yes', 'she', 'loves', 'you',
#                  'and', 'you', 'know', 'you', 'should', 'be', 'glad',
#
#                  'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#                  'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#                  'with', 'a', 'love', 'like', 'that',
#                  'you', 'know', 'you', 'should', 'be', 'glad',
#                  'with', 'a', 'love', 'like', 'that',
#                  'you', 'know', 'you', 'should', 'be', 'glad',
#                  'with', 'a', 'love', 'like', 'that',
#                  'you', 'know', 'you', 'should', 'be', 'glad',
#                  'yeah', 'yeah', 'yeah',
#                  'yeah', 'yeah', 'yeah', 'yeah'
#                  ]
#
# # 命名一个叫beatles的字典存储统计词频结果
# beatles = lyrics_to_frequencies(she_loves_you)
#
#
# def most_common_words(freqs):
#     values = freqs.values()
#     # 找到词频最高的那个值
#     best = max(freqs.values())
#     # 创建一个空列表
#     words = []
#     # 把词频最高的词提取出来，由于可能不止一个，所以用列表存储
#     for k in freqs:
#         if freqs[k] == best:
#             words.append(k)
#     return (words, best)
#
#
# # 找到至少出现了minTimes次的词
# def words_often(freqs, minTimes):
#     result = []
#     done = False
#     while not done:
#         # temp: tuple[list, Any]
#         temp = most_common_words(freqs)
#         # most_common_words函数里的best，即最高词频
#         if temp[1] >= minTimes:
#             # 如果该词词频大于minTimes，把加temp入到结果列表里
#             result.append(temp)
#             # 把前面找到的词频最高的词从字典freqs里删除，下一次循环不再重复计算这些词，则等同于计算词频第二高的词
#             for w in temp[0]:
#                 del (freqs[w])  # remove word from dict
#         else:
#             done = True
#     return result
#
#
# print(words_often(beatles, 5))
#
# #####################################
# # EXAMPLE: comparing fibonacci using memoization
# #####################################
#
# two base cases
# calls	itself twice
#
# def fib(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         # 每次计算都要把所有计算过的值都调用函数计算一遍
#         return fib(n - 1) + fib(n - 2)
#
#

"""
But note that this only works for procedures without side effects
# (i.e., the procedure will always produce the same	result for a specific argument
# independent of any other computations between calls)
"""
def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n - 1, d) + fib_efficient(n - 2, d)
        d[n] = ans
        return ans


# 初始化d字典，即fib(1)=1, fib(2)=2，把计算过的值存储在字典d里，下次计算时直接从字典里取值
d = {1: 1, 2: 2}

argToUse = 34
# print("")
# print('using fib')
# print(fib(argToUse))
# print("")
print('using fib_efficient')
print(fib_efficient(argToUse, d))
