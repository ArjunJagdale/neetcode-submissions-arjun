class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        i = j = length = 0
        
        while i < len(s) and j < len(s):
            if s[j] not in res:
                res.add(s[j])
                curr = len(res)
                j += 1
            else:
                curr = len(res)
                res = set()
                i += 1
                j = i

            length = max(length, curr)
        return length


        

