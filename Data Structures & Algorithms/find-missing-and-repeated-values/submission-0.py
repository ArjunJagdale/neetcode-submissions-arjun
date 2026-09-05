class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        hs = {}
        res_set = set()
        res = []

        for g in grid:
            for gs in g:
                res_set.add(gs)
                hs[gs] = hs.get(gs, 0) + 1
                if hs[gs] == 2:
                    res.append(gs)

        for i in range(1, n*n+1):
            if i not in res_set:
                res.append(i)
        
        return res