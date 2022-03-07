""" 
    Math.py will hold all the math related functions
    gcd --> gcd accepcts two numbers  num1 and num2 and returns gcd for the given numbers
"""

def gcd(num1, num2):
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)


if __name__ == "__main__":
    print(gcd(7,11))