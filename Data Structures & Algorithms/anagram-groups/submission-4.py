class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        frequency_map = {}

        def frequency(string):
            arr = [0]*26
            for char in string:
                arr[(ord(char)-97)]+=1
            return tuple(arr)

        for string in strs:
            freq = frequency(string)
            if freq in frequency_map:
                frequency_map[freq].append(string)
            else:
                frequency_map[freq] = [string]

        return [x for x in frequency_map.values()]