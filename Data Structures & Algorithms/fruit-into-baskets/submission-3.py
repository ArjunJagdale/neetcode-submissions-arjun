class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, res = 0, 0
        count = defaultdict(int)

        for i in range(len(fruits)):
            count[fruits[i]] += 1

            if len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    count.pop(fruits[l])
                
                l += 1
        
        return len(fruits) - l