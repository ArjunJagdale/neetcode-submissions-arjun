class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hm = {}
        res = []

        for i in arr:
            hm[i] = hm.get(i, 0) + 1 # {'d': 1, 'b': 2, 'c': 2, 'a': 1}
        
        for i in hm:
            if hm[i] == 1:
                res.append(i) # ['d', 'a']
                if len(res) >= k: # len(res) is 2 and equal to 2
                    return res[k-1]
        
        return ""


        
        

        
        
        