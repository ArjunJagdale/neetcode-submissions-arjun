class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        vocab = [0]*26
        vocabx = [0]*26

        if n1 > n2:
            return False
        
        for i in range(len(s1)):
            vocab[ord(s1[i])-ord("a")] += 1
            vocabx[ord(s2[i])-ord("a")] += 1
        
        if vocab == vocabx:
            return True
        
        for i in range(n1, n2):
            vocabx[ord(s2[i])-ord("a")] += 1
            vocabx[ord(s2[i-n1])-ord("a")] -= 1
            print(vocabx, ord(s2[i-n1]))

            if vocab == vocabx:
                return True

        return False