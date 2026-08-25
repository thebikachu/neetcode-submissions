from operator import add, sub, mul, truediv

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tok_map = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": truediv
        }

        stack = []

        for tok in tokens:
            if tok not in tok_map:
                # num
                stack.append(int(tok))

            else:
                num_1 = stack.pop()
                num_2 = stack.pop()

                result = tok_map[tok](num_2, num_1)

                if(tok == "/"):
                    result = int(result)

                stack.append(result)

        return stack[-1]