class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=len(nums)
        s1=set(nums)
        s2=len(s1)
        if s==s2:
            return False
        else:
            return True