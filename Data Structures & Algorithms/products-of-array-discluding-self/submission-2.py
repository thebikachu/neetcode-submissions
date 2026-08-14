class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [None] * len(nums)

        prefix = 1

        for idx, num in enumerate(nums):
            arr[idx] = prefix
            prefix = prefix * num

        prefix = 1
        for i in range(len(nums)-1, -1, -1):
            arr[i] *= prefix
            prefix = prefix*nums[i]

        return arr