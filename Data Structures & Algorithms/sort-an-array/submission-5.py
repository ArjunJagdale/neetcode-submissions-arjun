class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            
            n = len(nums)

            mid = n // 2
            left = nums[:mid]
            right = nums[mid:]

            sortedLeft = mergeSort(left)
            sortedRight = mergeSort(right)

            return merge(sortedLeft, sortedRight)
        
        def merge(left, right):
            i = j = 0
            res = []

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i = i + 1
                else:
                    res.append(right[j])
                    j = j + 1
                
            res.extend(left[i:])
            res.extend(right[j:])

            return res

        result = mergeSort(nums)

        return result