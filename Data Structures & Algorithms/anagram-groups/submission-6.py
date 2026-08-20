class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def frequency(string):
            chars = [0]*26

            for char in string:
                idx = ord(char)-97
                chars[idx] += 1

            return tuple(chars)

        str_frequencies = {}

        for string in strs:
            freq = frequency(string)
            if freq not in str_frequencies:
                str_frequencies[freq] = [string]
            else:
                str_frequencies[freq].append(string)

        return [x for x in str_frequencies.values()]