class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        def mergesort(people):
            n = len(people)

            if  n <= 1:
                return people
            
            mid = n // 2
            left = mergesort(people[:mid])
            right = mergesort(people[mid:])

            return merge(left, right)
        
        def merge(left, right):
            i = j = 0
            res = []

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            
            res.extend(left[i:])
            res.extend(right[j:])

            return res
        
        # solution
        people = mergesort(people)

        i = 0
        j = len(people) - 1
        count = 0 
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
                count += 1
            else:
                j -= 1
                count += 1
        
        return count




