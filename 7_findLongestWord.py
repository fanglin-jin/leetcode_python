'''
Project: leetcode_python
Author: jinfanglin
Date: 2020/11/16
'''
def findLongestStr(target,arr):
    length = 0
    index = -1
    for i in range(len(arr)):
        lengthofstr = compare(target,arr[i])
        if length < lengthofstr:
            length = lengthofstr
            index = i
    return arr[index]
def compare(s1,s2):
    i,j = 0,0
    tmpStr = ''
    while i<len(s1) and j<len(s2):
        if s1[i] == s2[j]:
            tmpStr += s1[i]
            i+=1
            j+=1
        else:
            i+=1
    return len(tmpStr)
if __name__ == "__main__":
    s = "abpcplea"
    d = ["ale","apple","monkey","plea"]
    print(findLongestStr(s,d))

