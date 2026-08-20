from operator import add,sub,mul,truediv
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": truediv
        }

        for tok in tokens:
            if tok in ops:
                if stack and len(stack) >= 2:
                    num_2 = stack.pop()
                    num_1 = stack.pop()
                    result = ops[tok](num_1, num_2)

                    if tok == "/":
                        stack.append(int(result))
                    else:
                        stack.append(result)
                else:
                    print("BAD")
            else:
                stack.append(int(tok))


        return stack[-1]