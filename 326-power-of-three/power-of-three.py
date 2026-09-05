class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        power=1
        while power<=n:
            if power == n:
                return True
                break
            power*=3    
        else:
            return False        