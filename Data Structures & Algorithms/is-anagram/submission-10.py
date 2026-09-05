class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hash_1 = {}

        for i in s:
            hash_1[i] = hash_1.get(i, 0) + 1
        
        for i in t:
            if i not in hash_1 or hash_1[i] == 0:
                return False

            hash_1[i] -= 1
        
        return True