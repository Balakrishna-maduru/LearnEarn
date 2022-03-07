from heapq import *
import math


class FindMinMax:
    def __init__(self, arr, k) -> None:
        self.arr = arr
        self.n = len(arr)
        self.k = k

    def find_k_th_smallest_number(self):
        "Brute-force way of finding"
        previous_min_number, previous_min_number_index = -math.inf, -1
        current_min_number, current_min_number_index = math.inf, -1
        for i in range(self.k):
            for j in range(self.n):
                print(
                    f"{i}, {j}, {previous_min_number},{previous_min_number_index},{current_min_number},{current_min_number_index}")
                if self.arr[j] > previous_min_number and self.arr[j] < current_min_number:
                    current_min_number = self.arr[j]
                    current_min_number_index = j
                elif self.arr[j] == previous_min_number and j > previous_min_number_index:
                    current_min_number = self.arr[j]
                    current_min_number_index = j
                    break
            previous_min_number = current_min_number
            previous_min_number_index = current_min_number_index
            current_min_number = math.inf
        return previous_min_number

    def find_k_th_smallest_number_using_soring(self):
        "Brute-force using sorting"
        max_heap = []

        for i in range(3):


def find_k_min_element(arr, k):
    max_heap = []
    for i in range(k):
        heappush(max_heap, -arr[i])

    for j in range(k, len(arr)):
        if -arr[j] > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -arr[j])

    return -max_heap[0]


def partition(arr, start, end):
    if start == end:
        return start
    pivot = arr[end]
    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[start] = arr[start], arr[i]
            start += 1
    arr[start], arr[end] = arr[end], arr[start]
    return start


def find_k_min_element(arr, k, start, end):
    p = partition(arr, start, end)
    if p == k-1:
        return arr[p]
    if p > k-1:
        return find_k_min_element(arr, k, start, p-1)
    return find_k_min_element(arr, k,  p+1, end)


# arr = [4, 1, 6, 2, 9, -1]
# print(find_k_min_element(arr, 5, 0, 5))
# print(arr)

arr = [1, 5, 12, 2, 11, 5]
k = 3
fmm = FindMinMax(arr, k)
print(fmm.find_k_th_smallest_number())
