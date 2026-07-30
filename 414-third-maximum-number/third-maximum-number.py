class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num=set(nums)
        num1=list(num)
        num1.sort()
        if len(num1)>=3:
            return num1[-3]
        else:
            return num1[-1]    