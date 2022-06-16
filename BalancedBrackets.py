# https://www.hackerrank.com/challenges/balanced-brackets/problem?h_r=profile

def isBalanced(s):
    # Write your code here
    stack = []
    for c in s:
        #print(c)
        if c == '(':
            stack.append(0);
        elif c == ')':
            if len(stack) > 0 and stack[-1] == 0:
                stack.pop()
            else:
                return ('NO')
        elif c == '[':
            stack.append(2)
        elif c == ']':
            if len(stack) > 0 and stack[-1] == 2:
                stack.pop()
            else:
                return ('NO')
        if c == '{':
            stack.append(4)
        elif c == '}':
            if len(stack) > 0 and stack[-1] == 4:
                stack.pop()
            else:
                return ('NO')
    
    if len(stack) == 0:
        return ('YES')
    else:
        return ('NO')
