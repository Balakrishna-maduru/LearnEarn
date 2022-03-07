class BitwiseOperations:

    def __init__(self) -> None:
        pass

    def max_consecutive_ones(self, n):
        count = 0
        while (n != 0):
            n = (n & (n << 1))
            count = count+1
        return count

    def is_fibbinary_num(self, n):
        if ((n & (n >> 1)) == 0):
            return 1
        return 0
