# def summ(n):
#     new_summ=0
#     for i in n:
#         new_summ+= i
#     return new_summ
import random


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# def factorial(n):
#     result = 1
#     if n == 0:
#         return 1
#     else:
#         for i in range(1,n+1):
#             result *= i
#         return result


# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return -1


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


def shitlist_find(lst, target):
    for i in lst:
        for j in i:
            for h in j:
                if h == target:
                    return h
                else:
                    h += 1
