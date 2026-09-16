class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi=max(candies)
        a=[]
        for i in candies:
            b=i+extraCandies
            if b>=maxi:
                a.append(True)
            else:
                a.append(False)    
        return a        