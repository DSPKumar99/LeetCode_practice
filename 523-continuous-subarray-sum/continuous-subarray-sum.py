class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dict={0:-1}
        prefix=0
        for i,num in enumerate(nums):
            prefix+=num
            rem=prefix % k
            if rem in dict:
                ind= i - dict[rem]
                if ind>=2:
                    return True 
            else:
                dict[rem] =i       
        return False               