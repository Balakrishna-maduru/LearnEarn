# Python3 program to implement direct index
# mapping with negative values allowed.

# Searching if X is Present in the
# given array or not.
def search(X):

	if X >= 0:
		return has[X][0] == 1

	# if X is negative take the absolute
	# value of X.
	X = abs(X)
	return has[X][1] == 1

def insert(a, n):

	for i in range(0, n):
		if a[i] >= 0:
			has[a[i]][0] = 1
		else:
			has[abs(a[i])][1] = 1

# Driver code
if __name__ == "__main__":

	a = [-1,1, 9, -9, -5, -8, -2, -9, -9 ]
	n = len(a)

	MAX = 10
	
	# Since array is global, it is
	# initialized as 0.
	has = [[0 for i in range(2)]
			for j in range(MAX + 1)]
	print(has)
	insert(a, n)
	print(has)

	X = -5
	if search(X) == True:
		print("Present")
	else:
		print("Not Present")

# This code is contributed by Rituraj Jain
