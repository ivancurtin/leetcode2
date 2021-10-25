class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        ls = ''
        
        length = 0
        
        for c in s:
            if c in ls:
                ls = ls[(ls.index(c)+1):]
            ls += c
            length = max(length, len(ls))
        return length