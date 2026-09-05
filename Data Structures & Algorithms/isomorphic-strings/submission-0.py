class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_res = []
        t_res = []

        for idx in s:
            s_res.append(s.index(idx))

        for idx in t:
            t_res.append(t.index(idx))
        
        return s_res == t_res
        