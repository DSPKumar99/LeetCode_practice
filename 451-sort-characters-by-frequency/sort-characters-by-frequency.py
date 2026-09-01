class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        result=""
        for i in s:
            y=s.count(i)
            freq[i]=y
        while freq:
            max_char=max(freq,key=freq.get)
            result+=max_char*freq[max_char]
            del freq[max_char]    
        return result