class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def frequency(string):
            chars = [0] * 26

            for char in string:
                idx = ord(char)-97
                chars[idx] += 1
            return tuple(chars)

        hash_table = {}

        for string in strs:
            freq = frequency(string)

            if freq in hash_table:
                hash_table[freq].append(string)
            else:
                hash_table[freq] = [string]

        return [x for x in hash_table.values()]