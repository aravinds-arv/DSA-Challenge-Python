class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        p, preProd = 1, [1]
        for i in range(1, n):
            p *= nums[i - 1]
            preProd.append(p)

        p, suffProd = 1, [1]
        for i in range((n - 2), -1, -1):
            p *= nums[i + 1]
            suffProd.append(p)

        return [preProd[i] * suffProd[(n - 1) - i] for i in range(n)]
