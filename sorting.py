#!/bin/python3
'''
Python provides built-in sort/sorted functions that use timsort internally.
You cannot use these built-in functions anywhere in this file.

Every function in this file takes a comparator `cmp` as input which controls how the elements of the list should be compared against each other.
If cmp(a,b) returns -1, then a<b;
if cmp(a,b) returns  1, then a>b;
if cmp(a,b) returns  0, then a==b.
'''

import random
import collections

def cmp_standard(a,b):
    '''
    used for sorting from lowest to highest
    '''
    if a<b:
        return -1
    if b<a:
        return 1
    return 0


def cmp_reverse(a,b):
    '''
    used for sorting from highest to lowest
    '''
    if a<b:
        return 1
    if b<a:
        return -1
    return 0


def cmp_last_digit(a,b):
    '''
    used for sorting based on the last digit only
    '''
    return cmp_standard(a%10,b%10)


def _merged(xs, ys, cmp=cmp_standard):
    '''
    Assumes that both xs and ys are sorted,
    and returns a new list containing the elements of both xs and ys.
    Runs in linear time.
    '''
    return_lst = []
    x_len = len(xs)
    y_len = len(ys)
    
    i = 0
    j = 0

    while i != x_len and j != y_len:
        if (cmp == cmp_standard and xs[i] >= ys[j]) or (cmp == cmp_reverse and xs[i] <= ys[j]):
            return_lst.append(ys[j])
            j += 1
        elif (cmp == cmp_standard and ys[j] >= xs[i]) or (cmp == cmp_reverse and ys[j] <= xs[i]):
            return_lst.append(xs[i])
            i += 1

    if i == x_len and j == y_len:
        return return_lst
    elif i == x_len:
        for num in range(j, y_len):
            return_lst.append(ys[num])
        return return_lst
    elif j == y_len:
        for num in range(i, x_len):
            return_lst.append(xs[num])
        return return_lst
    
def merge_sorted(xs, cmp=cmp_standard):
    '''
    Merge sort is the standard O(n log n) sorting algorithm.
    Recall that the merge sort pseudo code is:

        if xs has 1 element
            it is sorted, so return xs
        else
            divide the list into two halves left,right
            sort the left
            sort the right
            merge the two sorted halves

    You should return a sorted version of the input list xs
    '''
    
    if len(xs) <= 1:
        return xs
    else:
        middle = len(xs) //2 
        merge_sorted(xs[:middle],cmp=cmp)
        merge_sorted(xs[middle:],cmp=cmp)

        return _merged(merge_sorted(xs[:middle],cmp=cmp), merge_sorted(xs[middle:],cmp=cmp),cmp=cmp)
def quick_sorted(xs, cmp=cmp_standard):
    '''
    Quicksort is like mergesort,
    but it uses a different strategy to split the list.
    Instead of splitting the list down the middle,
    a "pivot" value is randomly selected, 
    and the list is split into a "less than" sublist and a "greater than" sublist.

    The pseudocode is:

        if xs has 1 element
            it is sorted, so return xs
        else
            select a pivot value p
            put all the values less than p in a list
            put all the values greater than p in a list
            sort both lists recursively
            return the concatenation of (less than, p, and greater than)

    You should return a sorted version of the input list xs
    '''
    less = []
    equal = []
    greater = []

    if len(xs) <= 1:
        return xs
    else:
        p = xs[0]
        for num in xs:
            if num < p:
                less.append(num)
            elif num > p:
                greater.append(num)
            elif num == p:
                equal.append(num)

        l = quick_sorted(less, cmp=cmp)
        g = quick_sorted(greater, cmp=cmp)
        if cmp == cmp_standard:
            return l + equal + g
        elif cmp == cmp_reverse:
            return g + equal + l
def quick_sort(xs, cmp=cmp_standard):
    '''
    EXTRA CREDIT:
    The main advantage of quick_sort is that it can be implemented in-place,
    i.e. with O(1) memory requirement.
    Merge sort, on the other hand, has an O(n) memory requirement.

    Follow the pseudocode of the Lomuto partition scheme given on wikipedia
    (https://en.wikipedia.org/wiki/Quicksort#Algorithm)
    to implement quick_sort as an in-place algorithm.
    You should directly modify the input xs variable instead of returning a copy of the list.
    '''
    pass
