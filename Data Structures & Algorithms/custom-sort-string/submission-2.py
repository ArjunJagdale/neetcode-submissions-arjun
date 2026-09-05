class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ''

        for i in order:
            for j in s:
                if j == i:
                    res += j
        
        for i in s:
            if i not in order:
                res += i
        
        return res

        

        