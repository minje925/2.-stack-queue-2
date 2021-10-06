alist = list(input())
stack = []
past = ''
answer = 0
for a in alist:
    if not stack and a == '(':
        stack.append(a)
        past = a
            
    elif past == '(' and a == ')':
        #print("레이저")
        stack.pop()
        past = a
        answer += len(stack)
    
    elif a=='(':
        stack.append(a)
        past = a

    elif past == ')' and a ==')':
        stack.pop()
        answer += 1
        past = ')'

    #print(stack)
print(answer)
        
        




