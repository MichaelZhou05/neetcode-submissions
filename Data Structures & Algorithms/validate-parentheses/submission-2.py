class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 : return False
        stack = []
        for par in s :
            print(stack)
            match par :
                case "(" :
                    stack.append(1)
                case "{" :
                    stack.append(2)
                case "[" :
                    stack.append(3)
                case ")" :
                    if stack.pop() != 1 :
                        return False
                case "}" :
                    if stack.pop() != 2 :
                        return False
                case "]" :
                    if stack.pop() != 3 :
                        return False
        return True