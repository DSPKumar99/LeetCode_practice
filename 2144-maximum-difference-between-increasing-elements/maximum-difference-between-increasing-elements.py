class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=-1
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    x=nums[j]-nums[i]
                    maxi=max(maxi,x)
        return maxi