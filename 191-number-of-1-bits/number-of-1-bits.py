class Solution:
    def hammingWeight(self, n: int) -> int:
        a=f"{n:b}"
        b=a.count("1")
        return b