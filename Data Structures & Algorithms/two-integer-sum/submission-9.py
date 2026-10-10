class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_index = dict()
        for i in range(len(nums)):
            if nums[i] in diff_index:
                return [diff_index[nums[i]], i]
            current_diff = target - nums[i]
            diff_index[current_diff] = i

        return []
