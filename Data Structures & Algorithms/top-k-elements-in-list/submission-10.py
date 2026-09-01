class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {

        }

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for item, value in freq.items():
            buckets[value].append(item)

        needed = k
        output = []
        # print(buckets)
        for i in range(len(nums), -1, -1):
            # print(i)
            while needed > 0 and len(buckets[i]) > 0:
                output.append(buckets[i].pop())
                needed -= 1

        return output

            
        # print(freq)