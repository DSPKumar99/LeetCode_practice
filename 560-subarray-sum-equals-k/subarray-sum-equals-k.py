class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=0
        cnt=0
        dict={0:1}
        for i in nums:
            prefix+=i
            if prefix-k in dict:
                cnt+=dict[prefix-k]
            if prefix in dict:
                dict[prefix]+=1
            else:
                dict[prefix]=1
        return cnt            
        