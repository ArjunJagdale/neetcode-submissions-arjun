class Solution:
    def maxDifference(self, s: str) -> int:
        h = {}

        for i in s:
            h[i] = h.get(i, 0) + 1

        even = []
        odd = []

        for i in h.values():
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        
        diff1 = max(odd) - min(even)
        return diff1


        
