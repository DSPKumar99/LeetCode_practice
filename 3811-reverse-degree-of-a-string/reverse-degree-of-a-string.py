class Solution:
    def reverseDegree(self, s: str) -> int:
        reverse=['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']
        sum=0
        for i in range(len(s)):
            ind=reverse.index(s[i])
            ind+=1
            sum+=ind*(i+1)
        return sum    