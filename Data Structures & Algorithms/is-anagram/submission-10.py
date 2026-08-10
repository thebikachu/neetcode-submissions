class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_table = {}

        for char in s:
            hash_table[char] = hash_table.get(char, 0) + 1

        for char in t:
            hash_table[char] = hash_table.get(char, 0 ) - 1

        return all([x == 0 for x in hash_table.values()])