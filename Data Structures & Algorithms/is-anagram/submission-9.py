class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_set = {}

        for char in s:
            hash_set[char] = hash_set.get(char, 0) + 1

        for char in t:
            hash_set[char] = hash_set.get(char, 0) - 1

        return all(count == 0 for count in hash_set.values())
