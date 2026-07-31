class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum=0
        cnt=0
        l=0
        r=k-1
        for i in range(0,r+1):
            sum+=arr[i]
        if sum/k>=threshold:
            cnt+=1
        while r<len(arr)-1:
            sum-=arr[l]
            l+=1
            r+=1
            sum+=arr[r]
            if sum/k>=threshold:
                cnt+=1    
        return cnt        