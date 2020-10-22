
# "(a(b(c)d)"
# "))(("

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        
        sNew = s
        for i, c in enumerate(s):
            print(sNew)
            if (c == '('):
                stack.append((')', i))
            elif (c == ')'):
                if (len(stack) == 0 or stack.pop()[0] != ')'):
                    sNew = sNew[:i] + '|' + sNew[i+1:]

        while(len(stack) != 0):
            _, i = stack.pop()
            sNew = sNew[:i] + '|' + sNew[i+1:]

        sNew = sNew.replace('|', '')               
        return sNew
                     
                    
sol = Solution()
print(sol.minRemoveToMakeValid("a)b(c)d"))
print(sol.minRemoveToMakeValid("))(("))