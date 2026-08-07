class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums = {}

        for idx, num in enumerate(nums):
            need = target - num

            if need in seen_nums:
                return [seen_nums[need], idx]

            seen_nums[num] = idx

        