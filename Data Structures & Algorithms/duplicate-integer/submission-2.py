class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        emp_set = set()

        for i in nums:
            if i in emp_set:
                return True
            emp_set.add(i)
        
        return False



         