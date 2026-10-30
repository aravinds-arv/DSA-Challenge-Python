class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for b in s:
            if b == "(" or b == "[" or b == "{":
                stack.append(b)
            elif stack == []:
                return False
            elif b == ")":
                if stack[-1] != "(":
                    return False
                stack.pop()
            elif b == "]":
                if stack[-1] != "[":
                    return False
                stack.pop()
            elif b == "}":
                if stack[-1] != "{":
                    return False
                stack.pop()

        return stack == []
