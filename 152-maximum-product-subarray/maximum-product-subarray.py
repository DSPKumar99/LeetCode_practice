class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pro=nums[0]
        maxi=nums[0]
        mini=nums[0]
        n=len(nums)
        for i in range(1,n):
            if nums[i]<0:
                maxi,mini=mini,maxi
            maxi=max(nums[i],maxi*nums[i])
            mini=min(nums[i],mini*nums[i])
            pro=max(pro,maxi)    
        return pro        