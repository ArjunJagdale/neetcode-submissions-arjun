class Solution:
    def customSortString(self, order: str, s: str) -> str:
        h = {}

        for i in order:
            if i in s:
                h[i] = h.get(i, 0) + 1
        
        res = ""    

        h2 = {}
        for x in s:
            if x not in order:
                res += x
            h2[x] = h2.get(x, 0) + 1
    

        for i in h:
            while h2[i] > 0:
                res += i
                h2[i] -= 1
        
        return res


        

        