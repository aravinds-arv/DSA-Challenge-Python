class Solution:
    def sortColors(self, nums: List[int]) -> None:
        countArr = [0 for _ in range(3)]
        
        for num in nums:
            countArr[num] += 1

        index = 0
        for key in range(len(countArr)):
            for _ in range(countArr[key]):
                nums[index] = key
                index += 1
            