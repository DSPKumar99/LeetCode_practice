class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=set(nums)
        maxi=0
        dict={}
        for i in a:
            y=nums.count(i)
            dict[i]=y
        ans=[]
        for j in range(k):
            max_key=list(dict.keys())[0]  #[0] is for 0th index
            for key in dict:
                if dict[key]>dict[max_key]:
                    max_key=key
            ans.append(max_key)
            del dict[max_key]
        return ans    