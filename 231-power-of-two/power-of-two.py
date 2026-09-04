class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power=1
        if n==1:
            return True
        while power<=n:
            if power == n:
                return True
                break
            power*=2    
        else:
            return False    