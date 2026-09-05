class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hm = {}
        unique = ""

        for i in s:
            hm[i] = hm.get(i, 0) + 1
            if i not in set(order):
                unique += i

        res = ""
        for i in order:
            if i in hm:
                while hm[i]:
                    hm[i] -= 1
                    res += i
        
        return res+unique