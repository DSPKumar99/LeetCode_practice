class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        cnt=0
        s=set()
        for x in nums:
            if x in s:
                continue
            s.add(x)    
            positions=[]
            for i in range(len(nums)):
                if nums[i]==x:
                    positions.append(i)
            if len(positions)==3:
                gap1=positions[1]-positions[0]
                gap2=positions[2]-positions[1]
                if gap1==gap2:
                    cnt+=1
        return cnt        