class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candys=set(candyType)
        total=len(candyType)
        unique=len(candys)
        should=total//2
        if unique==total:
            return should
        elif unique>=should:
            return should
        else:
            return unique