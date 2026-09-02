class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums2=[]
        if len(nums1)==1:
            return True
        odd=None
        for i in range(len(nums1)):
            if nums1[i]%2!=0:
                odd=nums1[i]
                break
        if odd is None:
            return True
        for i in range(len(nums1)):
            if nums1[i]%2==0:
                nums2.append(nums1[i]-odd)
            else:
                nums2.append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i]%2==0:
                return False
        return True                                     
