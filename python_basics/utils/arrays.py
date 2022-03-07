
boot = [6,3,1,5,2]
node = [3,1,2,5,4] 
t = 30
def find_cluster(node, boot,t, i,j):
    if i > j:
        return -1
    else:
        k = j-i
        sum_v = sum(node[i:j])
        max_v = max(boot[i:j])
        actual_v = max_v + sum_v * k
        print(f"i : {i}, j: {j}")
        print(f"sum = {sum_v}, max : {max_v}, actual : {actual_v}, k : {k}")
        if actual_v < t:
            return k
        else:
            l = find_cluster(node, boot,t, i,j-1)
            if l > 0:
                return l 
            r = find_cluster(node, boot,t, i+1,j)
            if r > 0:
                return r
            else: 
                return -1

print(find_cluster(node, boot,t, 0,len(node)))