class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for d in details:
            a = int(d[11:13])
            if a > 60:
                count += 1
        
        return count