
N = 10
l = [0]*N
print(f"Generate 10 zeros in list {l}")

l = [j for j in range(N)]
print(f"Generate 0 to {N} in list {l}")

l = [[i for i in range(N)] for j in range(N)]
print(f"Generate {N}X{N} matrix {l}")

l = [[i for i in range(1, j+1)] for j in range(1, N+1)]
print(f"Generate pyramid matrix {l}")
