class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=(low+high)//2
            no_days=canfinish(weights,days,mid)   #if canfinish(weights,day,mid):
            if no_days:
                high=mid
            else:
                low=mid+1
        return low
def canfinish(weights,days,cap):
    load=0
    req_days=1
    for weight in weights:
        if load+weight<=cap:
            load+=weight
        else:
            req_days+=1
            load=weight
    return req_days<=days                    