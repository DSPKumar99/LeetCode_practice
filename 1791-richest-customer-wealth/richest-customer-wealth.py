class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum=0
        a=[]
        maxi=0
        for l in accounts:
            z=0
            sum=0
            for i in l:
                z+=i
            sum+=z
            a.append(sum)
            maxi=max(a)
        return maxi    
