def reverseVowels(s_str):
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    s = [i for i in s_str]
    i=0
    j=len(s)-1
    while i<=j:
        if s[i] in vowels and s[j] in vowels:
            tmp = s[j]
            s[j] = s[i]
            s[i] = tmp
            i+=1
            j-=1
        elif s[i] in vowels and s[j] not in vowels:
            j-=1
        else:
            i+=1
    return str(s)
if __name__ == "__main__":
    s = "leetcode"
    print(reverseVowels(s))