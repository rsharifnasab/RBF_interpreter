import sys
commands = [  "[" , "]" , "<" , ">" , "+" , "-" , "." , "," ]




def execute(inp_file):
    try:
        inp = open(inp_file,"r")
    except:
        print("fatal error, file not found")
        exit()

    m = inp.read()
    c = []
    for i in range(len(m)):
        if m[i] in commands : c.append(m[i])
    print(c)



def main():
    if len(sys.argv) == 2: execute(sys.argv[1])
    else: print("Usage:", sys.argv[0], "filename")


main()
