import sys
commands_list = [  "[" , "]" , "<" , ">" , "+" , "-" , "." , "," ]
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
    global pointer
    if pointer>0 :
        pointer-=1
        return True
    return False;

def right():
    global pointer
    pointer+=1
    if pointer <= len(mem):
        mem.append(0)
    return True

def print_char():
    print((mem[pointer]),end=" ")

def run(commands,first=0,last=None):
    if(last==None): last = len(commands)
    commands_2run = commands[first:last]
    for c in commands_2run:
        print(c,end= " ")
        if (c=="+") : plus()
        if (c=="-") : minus()
        if (c=="<") : left()
        if (c==">") : right()
        if (c==".") : print_char()


def execute(inp_file):
    try:
        inp = open(inp_file,"r")
    except:
        print("fatal error, file not found")
        exit()

    all_input = inp.read()
    meanful_commands = []
    for i in range(len(all_input)):
        if all_input[i] in commands_list : meanful_commands.append(all_input[i])
    run(meanful_commands,0,len(meanful_commands))



def main():
    if len(sys.argv) == 2: execute(sys.argv[1])
    else: print("Usage:", sys.argv[0], "filename")


main()
