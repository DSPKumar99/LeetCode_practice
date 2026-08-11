class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pre=-1
        cur=0
        cnt=0
        for i in range(len(s)):
            if s[i] in t[pre+1:]:
                cur=t.index(s[i],pre+1) 
                if pre<cur:
                    cnt+=1
                    pre=cur
                else:
                    break    
        if cnt==len(s):
            return True  
        else:
            return False              