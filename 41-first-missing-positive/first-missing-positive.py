class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans=1
        y=set(nums)
        for i in range(1,len(y)+1):
            if ans in y:
                ans+=1 
            else:
                return ans    
        return ans        