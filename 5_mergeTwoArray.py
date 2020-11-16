'''
Project: leetcode_python
Author: jinfanglin
Date: 2020/11/16
'''

def merge(arr1,arr2):
    arr1.sort()
    arr2.sort()
    arr = [0 for i in range(len(arr1)+len(arr2))]
    i = 0
    j = 0
    k = 0
    while i<len(arr1) and j<len(arr2):
        if arr1[i] <= arr2[j]:
            arr[k]=arr1[i]
            k += 1
            i+= 1
        else:
            arr[k] = arr2[j]
            k += 1
            j+=1
    if i==len(arr1) and j<len(arr2)-1:
        arr[i+j:]=arr2[j:]
    elif j==len(arr2) and i<len(arr1)-1:
        arr[i+j:] = arr1[i:]
    return arr
if __name__ == "__main__":
    arr1 = [1,2,3]
    arr2 = [2,5,6]
    print(merge(arr1,arr2))
