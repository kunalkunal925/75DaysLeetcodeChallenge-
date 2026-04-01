class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(float(a) / b)
        }

        for token in tokens:
            if token in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                result = operators[token](num1, num2)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]