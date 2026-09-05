class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)-1
        res = 0

        while l <= r:
            cap = limit - people[r] # 1
            r -= 1 # 1
            res += 1 # 3
            if l <= r and cap >= people[l]:
                l += 1 # 1
        
        return res

