#Question 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elems = set()
        for elem in nums:
            if elem in elems:
                return True
            else:
                elems.add(elem)
        return False

