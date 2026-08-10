import ast
import operator


class Calculator:
    """Safe calculator for JARVIS."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"

        return a / b

    def calculate(self, expression: str):
        """
        Safely evaluate a basic mathematical expression.
        Supports +, -, *, /, %, and **.
        """

        operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Mod: operator.mod,
            ast.Pow: operator.pow,
        }

        def evaluate(node):
            if isinstance(node, ast.Expression):
                return evaluate(node.body)

            if isinstance(node, ast.Constant):
                if isinstance(node.value, (int, float)):
                    return node.value

                raise ValueError("Invalid value")

            if isinstance(node, ast.BinOp):
                operation = operators.get(type(node.op))

                if operation is None:
                    raise ValueError("Unsupported operator")

                left = evaluate(node.left)
                right = evaluate(node.right)

                if isinstance(node.op, ast.Div) and right == 0:
                    raise ValueError("Cannot divide by zero")

                return operation(left, right)

            if isinstance(node, ast.UnaryOp):
                value = evaluate(node.operand)

                if isinstance(node.op, ast.USub):
                    return -value

                if isinstance(node.op, ast.UAdd):
                    return value

                raise ValueError("Unsupported unary operator")

            raise ValueError("Invalid expression")

        try:
            tree = ast.parse(expression, mode="eval")
            return evaluate(tree)

        except ZeroDivisionError:
            return "Cannot divide by zero"

        except (SyntaxError, ValueError, TypeError):
            return "Invalid calculation"