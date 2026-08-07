class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=0
        r=0
        sum=0
        s=set()
        maxi=0
        for r in range(len(nums)):
            while nums[r] in s:
                s.remove(nums[l])
                sum-=nums[l]
                l+=1
            s.add(nums[r])
            sum+=nums[r]
            maxi=max(maxi,sum)
        return maxi