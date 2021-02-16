class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)%2 != 0:
            return False

        stack = []

        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)

            else:
                #print("stack :", stack)
                if not stack:
                    return False
                last_char_from_stack = stack.pop()
                #print("last_char_from_stack:", last_char_from_stack)
                #print("char:",char)
                if last_char_from_stack == '(' and char != ")": 
                    return False
                if last_char_from_stack == '{' and char != "}": 
                    return False
                if last_char_from_stack == '[' and char != "]": 
                    return False

        if stack:
            return False
        return True






