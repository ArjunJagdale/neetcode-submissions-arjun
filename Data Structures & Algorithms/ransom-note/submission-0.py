class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h = {}
        for i in magazine:
            h[i] = h.get(i, 0) + 1
        
        for x in ransomNote:
            if x not in h or h[x] == 0:
                return False
            
            h[x] -= 1
        
        return True