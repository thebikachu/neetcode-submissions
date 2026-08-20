class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {
            "{": "}",
            "[": "]",
            "(":")"
        }

        stack = []

        for char in s:
            if char in char_map:
                # LHS
                stack.append(char)
                continue

            print(char)
            if char not in char_map:
                if not stack:
                    return False
                # RHS
                prev_char = stack.pop()
                print(char_map[prev_char], char)
                if char_map[prev_char] != char:
                    return False


        if len(stack) == 0:
            return True
        else:
            return False