def precedence(char):
    if char=="+" or char=="-":
        return 1
    elif char=="*" or char=="/":
        return 2
    return 0
def is_Operator(c):
    return c.isalpha() or c.isdigit()
def infix_postfix(exp):
    postfix=[]
    stack=[]
    for i in exp:
        if is_Operator(i):
            postfix.append(i)
        elif i=="(":
            stack.append(i)
        elif i==")":
            while stack and stack[-1]!="(":
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1])>=precedence(i):
                postfix.append(stack.pop())
            stack.append(i)
    while stack:
        postfix.append(stack.pop())
    return "".join(postfix)
            
            
expression = "A+B*(C-D)"
result = infix_postfix(expression)
print("Postfix expression:", result)
        