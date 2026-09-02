class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = {}

        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        for x in t:
            if x not in hashmap or hashmap[x] == 0:
                return False
            hashmap[x] -= 1
        
        return True