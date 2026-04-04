class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        vocab = [0] * 26
        for i in range(len(s1)):
            vocab[ord(s1[i])-ord("a")] += 1
        
        i = 0
        while i < len(s2):
            vocabx = [0] * 26
            for x in range(i, i+len(s1)):
                if i+len(s1) <= len(s2):
                    vocabx[ord(s2[x])-ord("a")] += 1
                if vocab == vocabx:
                    return True
            i += 1
        return False