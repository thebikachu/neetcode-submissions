class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = {}

        for idx, num in enumerate(nums):
            wanted = target-num
            if wanted in needed:
                return [needed[wanted], idx]

            needed[num] = idx
            