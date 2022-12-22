def create_Stack():
    return []
def push(item,s):
    s.append(item)
def Pop(s):
    return s.pop()
def Top(s):
    return s[-1]
def is_empty(s):
    return s == []

def postfix_eval(exp):
    #3 4 + 5 6 + *
    stack = create_Stack()
    exp = exp.split(" ")
    for token in exp:
        if token.isdigit(): push(token,stack)
        else:
            op2 = Pop(stack)
            op1 = Pop(stack)
            result = str(eval(op1 + token + op2))
            push(result, stack)

    return Pop(stack)

print(postfix_eval("3 4 + 5 6 + *"))

def create_queue():
    return []
def enqueue(item,q):
    q.append(item)
def dequeue(q):
    return q.pop(0)
def front(q):
    return q[0]
def is_empty(q):
    return q == []