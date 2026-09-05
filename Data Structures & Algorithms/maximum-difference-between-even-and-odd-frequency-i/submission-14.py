class Solution:
    def maxDifference(self, s: str) -> int:

        h = {}

        for i in s:
            h[i] = h.get(i, 0) + 1

        max_c = 0
        min_c = float('inf')

        for i in h:
            if h[i] % 2 != 0 and h[i] > max_c:
                max_c = h[i]
            elif h[i] % 2 == 0 and h[i] < min_c:
                min_c = h[i]

        if max_c < min_c:
            return max_c - min_c
        return abs(max_c - min_c)
        


        
