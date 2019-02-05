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

def end_index_finder(commands):
    t = 0
    for i in range(len(commands)):
        if commands[i] == '[': t+=1
        if commands[i] == ']': t-=1
        if t==0 :
            #print("end index is : ",i)
            return i # todo



def bf_main(commands):
    this_index = 0
    loop_begin = []
    while  this_index < len(commands):
        c = commands[this_index]
        #print(c,end= " ")
        if (c=="+") : plus()
        if (c=="-") : minus()
        if (c=="<") : left()
        if (c==">") : right()
        if (c==".") : print_char()
        if (c=="[") :
            end_index = this_index + end_index_finder(commands[this_index:])
            print(" [ detected, first:",this_index," last = ",end_index)
            if(mem[pointer]==0):
                this_index = end_index+1
                print("false, skipping")
            else:
                loop_begin.append(this_index)
                print("true, this_index saved")
        if (c=="]") :
            print("this index = ",this_index)
            print(loop_begin)
            this_index = loop_begin.pop()
            print("end of loop going to ",this_index," value= ",commands[this_index])
        this_index+=1

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
    bf_main(meanful_commands)



def main():
    if len(sys.argv) == 2: execute(sys.argv[1])
    else: print("Usage:", sys.argv[0], "filename")


main()
