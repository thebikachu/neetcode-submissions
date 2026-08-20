class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        freq_buckets = [[] for _ in range(len(nums)+1)]

        for item, val in freq.items():
            freq_buckets[val].append(item)

        ret = []
        needed = k
        for i in range(len(freq_buckets)-1, -1, -1):
            if not freq_buckets[i]:
                continue

            while needed > 0 and freq_buckets[i]:
                ret.append(freq_buckets[i].pop())
                needed -= 1

        return ret
