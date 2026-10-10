class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target - nums[i]) in nums:
                j = len(nums) - (nums[::-1].index((target - nums[i])) + 1)
                if i != j:
                    return [i, j]

        return []