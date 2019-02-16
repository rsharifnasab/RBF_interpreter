import sys
commands_list = [  "[" , "]" , "<" , ">" , "+" , "-" , "." , "," ]

translated = """

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
"""


def end_index_finder(commands):
    t = 0
    for i in range(len(commands)):
        if commands[i] == '[': t+=1
        if commands[i] == ']': t-=1
        if t==0 :
            #print("end index is : ",i)
            return i # todo



def bf_main(commands):
    global translated
    this_index = 0
    loop_begin = []
    ind_count = 0;
    while  this_index < len(commands):
        c = commands[this_index]
        #print(c,end= " ")
        indent = " " * ind_count
        if (c=="+") :  translated = translated + indent + "plus()\n"
        if (c=="-") :  translated = translated + indent + "minus()\n"
        if (c=="<") :  translated = translated + indent + "left()\n"
        if (c==">") :  translated = translated + indent + "right()\n"
        if (c==".") :  translated = translated + indent + "print_char()\n"
        if (c=="[") :
            translated = translated + indent + "while mem[pointer] > 0: \n"
            ind_count+=1
        if (c=="]") :
            ind_count-=1
        this_index+=1

def execute(inp_file):
    try:
        inp = open(inp_file,"r")
    except:
        print("fatal error, file not found")
        exit()
    global translated
    all_input = inp.read()
    meanful_commands = []
    for i in range(len(all_input)):
        if all_input[i] in commands_list : meanful_commands.append(all_input[i])
    bf_main(meanful_commands)





if len(sys.argv) == 2: execute(sys.argv[1])
else:
    print("Usage:", sys.argv[0], "filename")
    exit()
translated_file = open("out.py", "w")
translated_file.write(translated)
translated_file.close()
print("output file created in out.py")
