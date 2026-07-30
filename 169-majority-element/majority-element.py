class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        dict={}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+=1
            else:    
                dict[nums[i]]=1
            if dict[nums[i]]>n/2:
                return  nums[i]     
