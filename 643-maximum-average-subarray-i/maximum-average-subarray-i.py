class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        r=k-1
        maxi=0
        sum=0
        for i in range(l,r+1):
            sum=sum+nums[i]
            maxi=sum
        while r<len(nums)-1:
                sum=sum-nums[l]
                l+=1
                r+=1
                sum=sum+nums[r]
                maxi=max(maxi,sum)
        return maxi/k       