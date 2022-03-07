import math

class Array:
    def __init__(self):
        pass


    def roatate_left(self, arr, count_to_rotare):
        """
        Example 1:
            Input : roatate_left([1,2,3,4,5,6,7,8],2)
            Output : 
                count : 2, gcd : 2
                move : arr[0] <-- arr[2]
                move : arr[2] <-- arr[4]
                move : arr[4] <-- arr[6]
                move : arr[1] <-- arr[3]
                move : arr[3] <-- arr[5]
                move : arr[5] <-- arr[7]
                [3, 4, 5, 6, 7, 8, 1, 2]
        Example 2:
            Input : roatate_left([1,2,3,4,5,6,7,8,9],2
            Output : 
                count : 2, gcd : 1
                move : arr[0] <-- arr[2]
                move : arr[2] <-- arr[4]
                move : arr[4] <-- arr[6]
                move : arr[6] <-- arr[8]
                move : arr[8] <-- arr[1]
                move : arr[1] <-- arr[3]
                move : arr[3] <-- arr[5]
                move : arr[5] <-- arr[7]
        """

        lenth_of_array = len(arr)
        count_to_rotare = count_to_rotare % lenth_of_array
        gcd = math.gcd(lenth_of_array,count_to_rotare)
        print(f"count : {count_to_rotare}, gcd : {gcd}")
        for i in range(gcd):
            temp = arr[i]
            j = i
            while 1:
                k = j + count_to_rotare
                if k >= lenth_of_array:
                    k = k-lenth_of_array
                if k == i: 
                    break
                print(f"move : arr[{j}] <-- arr[{k}]")
                arr[j] = arr[k]
                j = k
            arr[j] = temp
        print(arr)


if __name__ == "__main__":
    array = Array()
    array.roatate_left([1,2,3,4,5,6,7,8,9],2)
