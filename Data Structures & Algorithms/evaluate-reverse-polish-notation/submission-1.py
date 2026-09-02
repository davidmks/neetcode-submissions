class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue
                
            b = stack.pop()
            a = stack.pop() 
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))
        
        return stack.pop()