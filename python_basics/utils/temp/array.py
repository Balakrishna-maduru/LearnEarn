


def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)


def lrotate(arr,d):
    length_of_arr = len(arr)
    d = d%length_of_arr
    g_c_d = gcd(d,length_of_arr)
    for i in range(g_c_d):
        temp = arr[i]
        j=i
        while 1:
            k = j+d
            if k >= length_of_arr:
                k = k-length_of_arr
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

arr = [1,2,3,4,5,6,7]
d=3
lrotate(arr,d)
print(arr)

