

mem = [0]
pointer = 0

def plus():
    mem[pointer]+=1

def minus():
    if mem[pointer]>0 :
        mem[pointer]-=1;
        return True;
    return False;

def left():
    #print("left ran")
    global pointer
    if pointer>0 :
        pointer-=1
        return True
    #print("returning false")
    return False;

def right():
    global pointer
    pointer+=1
    if pointer <= len(mem):
        mem.append(0)

def print_char():
    print(chr(mem[pointer]),end=" ")
right()
plus()
plus()
plus()
plus()
plus()
plus()
plus()
plus()
plus()
while mem[pointer] > 0: 
 left()
 plus()
 plus()
 plus()
 plus()
 plus()
 plus()
 plus()
 plus()
 right()
 minus()
left()
print_char()
right()
plus()
plus()
plus()
plus()
plus()
plus()
plus()
while mem[pointer] > 0: 
 left()
 plus()
 plus()
 plus()
 plus()
 right()
 minus()
left()
plus()
print_char()
plus()
plus()
plus()
plus()
plus()
plus()
plus()
print_char()
print_char()
plus()
plus()
plus()
print_char()
while mem[pointer] > 0: 
 minus()
right()
plus()
plus()
plus()
plus()
plus()
plus()
plus()
plus()
while mem[pointer] > 0: 
 left()
 plus()
 plus()
 plus()
 plus()
 right()
 minus()
left()
print_char()
right()
plus()
plus()
plus()
plus()
plus()
plus()
plus()
plus()
plus()
plus()
plus()
while mem[pointer] > 0: 
 left()
 plus()
 plus()
 plus()
 plus()
 plus()
 plus()
 plus()
 plus()
 right()
 minus()
left()
minus()
print_char()
minus()
minus()
minus()
minus()
minus()
minus()
minus()
minus()
print_char()
plus()
plus()
plus()
print_char()
minus()
minus()
minus()
minus()
minus()
minus()
print_char()
minus()
minus()
minus()
minus()
minus()
minus()
minus()
minus()
print_char()
while mem[pointer] > 0: 
 minus()
right()
plus()
plus()
plus()
plus()
plus()
plus()
plus()
plus()
while mem[pointer] > 0: 
 left()
 plus()
 plus()
 plus()
 plus()
 right()
 minus()
left()
plus()
print_char()
while mem[pointer] > 0: 
 minus()
plus()
plus()
plus()
plus()
plus()
plus()
plus()
plus()
plus()
plus()
print_char()
