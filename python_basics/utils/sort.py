
from datetime import datetime
class Sort:
    def __init__(self) -> None:
        self.arr = [2,1,6,3,9,0,-1]
        

    def bubble_sort(self,arr):
        n = len(arr)
        for i in range(n):
            flag = 0
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    flag = 1
            if flag == 0:
                break

    def selection_sort(self, arr):
        n =len(arr)
        for i in range(n):
            min_v = i
            for j in range(i+1, n):
                if arr[j] < arr[min_v]:
                    min_v = j
            arr[i], arr[min_v] = arr[min_v], arr[i]

    def insertion_sort(self, arr):
        n =len(arr)
        for i in range(1,n):
            key = arr[i]
            j = i-1
            while j >=0 and arr[j] > key:
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = key

    def merge(self, arr, lr,rr):
        i = j = k =0
        while i < len(lr) and j < len(rr):
            if lr[i] < rr[j]:
                arr[k] = lr[i]
                i+=1
            else:
                arr[k] = rr[j]
                j+=1
            k+=1
        while i < len(lr):
            arr[k] = lr[i]
            i+=1
            k+=1

        while j < len(rr):
            arr[k] = rr[j]
            j+=1
            k+=1

    def merge_sort(self, arr):
        n = len(arr)
        if n <2:
            return
        mid = int(n/2)
        lr = arr[:mid]
        rr = arr[mid:]
        self.merge_sort(lr)
        self.merge_sort(rr)
        self.merge(arr, lr,rr)

    def partition(self, arr, start, end):
        pivot = arr[end]
        pointer = start
        for i in range(start, end):
            if arr[i] <  pivot:
                arr[i], arr[pointer] = arr[pointer], arr[i]
                pointer+=1
        arr[pointer], arr[end] = arr[end], arr[pointer]
        return pointer

    def quick_sort(self, arr, start, end):
        if start > end:
            return
        pointer = self.partition(arr, start, end)
        self.quick_sort(arr,start,pointer-1)
        self.quick_sort(arr,pointer+1, end)


def sort_time(function):
    start = datetime.now()
    def call_sort():
        function()
    call_sort()
    end = datetime.now()
    print(f"Time takend for {function.__name__}: {end-start}")

arr = [2,1,6,3,9,0,-1]
@sort_time
def sort():
    s = Sort()
    s.merge_sort(arr)
print(arr)