class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r=s.rstrip()
        str=r[::-1]
        count=0
        for i in str:
            count+=1
            if i==" ":
                count-=1
                break
        return count     