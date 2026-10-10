class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n_uniques = 0
        for i in range(len(nums)):
            if nums[i] not in nums[:i]:
                n_uniques += 1
        
        return not (n_uniques == len(nums))