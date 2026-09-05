class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        hash_setA = {}
        hash_setB = {}

        for i in s:
            hash_setA[i] = hash_setA.get(i, 0) + 1
        

        for j in t:
            hash_setB[j] = hash_setB.get(j, 0) + 1

        return hash_setA == hash_setB
        
        




        