s=[]
top =None
def isEmpty(stack):
    if(stack==[]):
        return True
    else:
        return False

def push(stack,item):
    s.append(item)
    top =len(stack)-1

def spop(stack):
    if(isEmpty(stack)):
        return ('UnderFlow')
    else:
        i= stack.pop()
        if(len(stack)==0):
            top=None
        else:
            top=top-1
    return i

def display(stack):
    if(isEmpty(stack)):
        print("Stack is empty")
    else:
        top = len(stack)-1
        print(stack[top],"<--top")
        for i in range(top-1,-1,-1):
            print(stack[i])
while True:
    print("Choice are\n 1) Push\n 2) Pop\n 3) Display\n 4) Exit\n")
    a=int(input("Enter your choice"))
    if(a==1):
        item=int(input("Enter the number to push"))
        push(s,item)
        print("%d added number succesful" %item)
        input("Press any key to cont..")

    elif(a==2):
        item=spop(s)
        if(item=="Underflow"):
            print("Stack is empty")
        else:
            print("%d is pop"%item)
        input("Press any key to cont..")

    elif(a==3):
        display(s)
        input("Press any key to cont..")

    elif(a==4):
        break
    else:
        print("Wrong Choice")
        input("Press any key to cont..")




