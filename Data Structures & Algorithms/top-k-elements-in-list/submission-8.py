class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = {}

        for num in nums:
            freq_table[num] = freq_table.get(num, 0) + 1

        # print(freq_table)
        arr = [[] for _ in range(len(nums) + 1)]
        for item, freq in freq_table.items():
            # need to use [freq] to find frequency in array because freq alone looks for an integer
            arr[freq].append(item)

        # print(arr)
        ret = []
        needed = k
        for i in range(len(arr)-1, -1, -1):
            if(len(arr[i]) == 0):
                continue
            else:
                # for element in bucket
                for ele in arr[i]:
                    if needed == 0:
                        return ret
                    else:
                        ret.append(ele)
                        needed -= 1

        return ret