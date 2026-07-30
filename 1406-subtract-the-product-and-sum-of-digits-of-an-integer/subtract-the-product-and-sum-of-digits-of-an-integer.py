class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        m=str(n)
        sum=0
        pro=1
        for i in m:
            y=int(i)
            pro*=y
            sum+=y
        return pro-sum    