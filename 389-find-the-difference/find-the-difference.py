class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=list(s)
        for i in range(max(len(s),len(t))):
            if t[i]  in s:
                s.remove(t[i])
            else:
                return t[i]      