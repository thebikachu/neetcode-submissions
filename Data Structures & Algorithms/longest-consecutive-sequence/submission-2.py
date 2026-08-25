class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        maxLen = 0

        for num in numSet:
            if num - 1 not in numSet:
                # start

                length = 1
                curr = num + 1

                while curr in numSet:
                    length += 1
                    curr += 1

                if length > maxLen:
                    maxLen = length

        return maxLen