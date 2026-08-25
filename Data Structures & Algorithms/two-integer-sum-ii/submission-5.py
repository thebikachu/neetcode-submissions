class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while right > left:
            sumTwo = numbers[left]+numbers[right]
            if sumTwo == target:
                return [left+1, right+1]

            elif(sumTwo < target):
                left += 1
            elif(sumTwo > target):
                right -= 1

        return [left+1, right+1]

        