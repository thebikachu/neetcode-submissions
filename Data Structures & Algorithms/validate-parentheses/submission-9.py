class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        char_map = {
            "{": "}",
            "(": ")",
            "[": "]"
        }

        for char in s:
            if char in char_map:
                # means its a LHS char
                stack.append(char)
            else:
                # RHS char
                if len(stack) == 0:
                    return False
                LHS_char = stack.pop()
                if char_map[LHS_char] == char:
                    continue
                else:
                    return False

        return True if len(stack) == 0 else False