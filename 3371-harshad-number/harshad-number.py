class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        y=str(x)
        sum=0
        for i in y:
            z=int(i)
            sum+=z
        if x%sum==0:
            return sum
        else:
            return -1    