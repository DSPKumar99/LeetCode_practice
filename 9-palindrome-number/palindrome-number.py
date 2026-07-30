class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        p=y[::-1]
        if y==p:
            return True
        else:
            return False    
