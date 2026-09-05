class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        total = 0

        for i in range(len(operations)):
            if operations[i] == "+":
                x = int(res[-1]) + int(res[-2])
                res.append(x)
                total += x
            elif operations[i] == "D":
                x = int(res[-1]) * 2
                res.append(x)
                total += x
            elif operations[i] == "C":
                x = int(res[-1])
                res.pop()
                total -= x
            else:
                x = int(operations[i])
                res.append(x)
                total += x
        
        return total
