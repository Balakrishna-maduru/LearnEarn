def find_odd(arr):
    ret = []
    for i in arr:
        if not i ^ 1 == i + 1:
            ret.append(i)
    return ret


def odd_occuring_element(arr):
    ret = 0
    for i in arr:
        ret ^= i
    return ret

def find_missing_element(arr):
    n = len(arr)+1
    sum_of_numbers = 0
    for i in arr:
        sum_of_numbers = sum_of_numbers + i
    return (n*(n+1)/2) - sum_of_numbers


    #Function to find the maximum index difference.
    def max_index_diff(self,arr,n):
    
        #Constructing LMin[] such that LMin[i] stores the minimum value 
        #from (arr[0], arr[1], ... arr[i]).
        LMin=[0 for i in range(n)]
        LMin[0]=arr[0]
        #arr = [15,86,78,93,100,6]
        # [15, 15, 15, 15, 15, 6]
        for i in range(1,n):
            LMin[i] = min(arr[i],LMin[i-1])
        print(LMin)
        #Constructing RMax[] such that RMax[j] stores the maximum value 
        #from (arr[j], arr[j+1], ..arr[n-1]). 
        RMax=[0 for i in range(n)]
        RMax[n-1]=arr[n-1]
    
        for i in range(n-2,-1,-1):
            RMax[i]=max(arr[i],RMax[i+1])
        print(RMax)
        i,j,maxDiff=0,0,-1
        # #Traversing both arrays from left to right to find optimum j-i. 
        # #This process is similar to merge() of MergeSort.
        while j<n and i<n:
            if LMin[i]<=RMax[j]:
                #Updating the maximum difference.
                maxDiff=max(maxDiff,j-i)
                j=j+1
            else:
                i=i+1
        #returning the maximum difference.        
        return maxDiff


if __name__ == "__main__":
    arr = [1, 2, 4, 6, 3, 7, 8]
    # print(find_odd(arr))
    # print(odd_occuring_element(arr))
    print(find_missing_element(arr))
