def stack(arg1, arg2, arg3):
    if arg2 == "add":
        arg1.insert(arg3, 0)
    elif arg2 == "remove":
        arg1.pop(0)

def queue(arg1, arg2, arg3):
    if arg2 == "add":
        arg1.append(arg3)
    elif arg2 == "remove":
        arg1.pop(0)

num = [1, 2, 3]



print('Adding new element to the stack')
stack(num, "add", 0)
print(num) 
print('Adding remove an element from stack')
stack(num, "remove", 0)
print(num)
print('Adding new element to the queue')
queue(num, "add", 4)
print(num)  
print('Adding remove and element from the queue')
queue(num, "remove", 0)
print(num)  
