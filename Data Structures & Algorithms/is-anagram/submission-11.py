class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0)+1

        for char in t:
            freq[char] = freq.get(char, 0)-1

        return all([x == 0 for x in freq.values()])