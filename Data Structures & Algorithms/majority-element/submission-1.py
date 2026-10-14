from math import floor

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        threshold = floor(len(nums) / 2)

        nums.sort()

        count = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev:
                count += 1
                if count > threshold:
                    return nums[i]
            else:
                count = 1
            prev = nums[i]
