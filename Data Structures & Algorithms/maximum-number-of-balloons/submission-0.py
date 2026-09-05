class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ref = 'balon'
        hs = {}

        for i in text:
            if i in ref:
                hs[i] = hs.get(i, 0) + 1
        
        if len(hs) < 5:
            return 0
        
        hs['l'] //= 2
        hs['o'] //= 2

        return min(hs.values())