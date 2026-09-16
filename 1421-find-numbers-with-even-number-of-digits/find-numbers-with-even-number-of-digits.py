class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even=0
        for i in nums:
            count=0
            while i>0:
                count+=1
                i=i//10
            if count%2==0:
                even+=1
        return even         