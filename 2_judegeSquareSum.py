import math
def judegeSquareSum(target):
    i = 1
    j = int(math.sqrt(target))
    while i<=j:
        if i**2 + j**2 == target:
            return [i,j]
        if i**2+j**2 > target:
            j-=1
        if i**2 + j**2 < target:
            i+=1
    return -1
if __name__ == "__main__":
    print(judegeSquareSum(10))