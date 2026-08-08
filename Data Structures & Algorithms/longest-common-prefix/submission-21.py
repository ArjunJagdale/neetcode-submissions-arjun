class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])): # 3 -> 0, 1, 2
            for s in strs: # bat
                if i == len(s) or s[i] != strs[0][i]: # 
                    return s[:i]
        
        return strs[0]