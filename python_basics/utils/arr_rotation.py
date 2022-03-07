class Solution:
    def find_rpoint(self, a):
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                return i+1
        
    def binary_search(self, arr, ele):
        n = len(arr)
        mid = int(n//2)
        print(arr)
        print(mid)
        if ele == arr[mid]:
            return mid
        elif ele > arr[mid]:
            return self.binary_search(arr[mid:], ele)
        else:
            return self.binary_search(arr[:mid], ele)
        return -1

    
    def search(self, a : list, key : int):
        r_point = self.find_rpoint(a)
        print(r_point)
        left = a[:r_point]
        print(left)
        right = a[r_point:]
        print(right)
        return self.binary_search(left, key)
        return self.binary_search(right, key)

arr = [5,6,7,8,9,10,1,2,3]
s =Solution()
s.search(arr, 10)