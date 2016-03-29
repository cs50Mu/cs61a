#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

def subsets(lst, n):
    if n == 0:
        return [[]]
    if len(lst) == n:
        return [lst]
    use_first = [ [lst[0]]+x for x in subsets(lst[1:], n-1) ]
#    print use_first,n
    dont_use_first = subsets(lst[1:], n)
#    print dont_use_first,n
#    print use_first + dont_use_first,n
    return use_first + dont_use_first


def subsets_all(lst):
    if len(lst) == 0:
        return [[]]
    use_first = [ [lst[0]]+x for x in subsets_all(lst[1:]) ]
    print use_first
    dont_use_first = subsets_all(lst[1:])
    print dont_use_first
    print use_first + dont_use_first
    return use_first + dont_use_first
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']


print len(subsets(letters,2))
print subsets(letters,2)
#print subsets_all([1,2])
