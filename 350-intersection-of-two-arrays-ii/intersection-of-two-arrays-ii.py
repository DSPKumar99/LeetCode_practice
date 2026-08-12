class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num=[]
        smaller=min(nums1,nums2,key=len)
        if smaller is nums1:
            temp=nums2
        else:
            temp=nums1
        for i in smaller:
            if i in nums1 and i in nums2:
                num.append(i)
                temp.remove(i)  
        return num    