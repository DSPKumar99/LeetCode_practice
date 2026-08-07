class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a=set(arr)
        dict={}
        for i in a:
            y=arr.count(i)
            dict[i]=y
        c=list(dict.values())
        x=set(c)    
        if len(c)==len(x):
            return True
        else:
            return False    