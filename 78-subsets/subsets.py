class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        result=[]
        for i in range(2**n):
            subset=[]
            for j in range(n):
                if (i//(2**j))%2==1:
                    subset.append(nums[j])
            result.append(subset)
        return result