'''
Project: leetcode_python
Author: jinfanglin
Date: 2020-11-15
'''
def validPalindrome(s):
    i = 0
    j = len(s)-1
    while i<j:
        if s[i] != s[j]:
            return isPalindrome(s,i,j-1) or isPalindrome(s,i+1,j)
        else:
            i+=1
            j-=1
def isPalindrome(s,i,j):
    while i<j:
        if s[i]!=s[j]:
            return False
        else:
            i+=1
            j-=1
    return True
if __name__ == "__main__":
    s = "abca"
    print(validPalindrome(s))