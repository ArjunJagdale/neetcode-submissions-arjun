class Solution:
    def maxDifference(self, s: str) -> int:
        h = {}
        max_e = float("inf")
        max_o = 0

        for i in s:
            h[i] = h.get(i, 0) + 1

        for i in h:
            if h[i]%2==0 and h[i] < max_e:
                max_e = h[i]
            elif h[i]%2!=0 and h[i] > max_o:
                max_o = h[i]
                
        return max_o - max_e