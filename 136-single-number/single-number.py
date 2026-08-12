class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=set(nums)
        dict={}
        for i in a:
            y=nums.count(i)
            dict[i]=y
        for key,value in dict.items():
            if value==1:
                return key
