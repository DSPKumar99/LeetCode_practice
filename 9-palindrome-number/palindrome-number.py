class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        def f(i,x):
            if i>=len(x)/2:
                return True
            if x[i]!=x[len(x)-i-1]:
                return False
            return f(i+1,x)
        return f(0,x)    
