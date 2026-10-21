class Solution:
    def merge(self, A: List[int], B: List[int]) -> List[int]:
        n, m = len(A), len(B)
        C, i, j = [], 0, 0

        while i < n and j < m:
            if A[i] <= B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1

        while i < n:
            C.append(A[i])
            i += 1

        while j < m:
            C.append(B[j])
            j += 1

        return C

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        
        A = self.sortArray(nums[:n // 2])
        B = self.sortArray(nums[n // 2:])

        return self.merge(A, B)
