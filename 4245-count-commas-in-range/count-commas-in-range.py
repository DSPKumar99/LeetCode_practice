class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        else:
            a=n-1000
            return a+1