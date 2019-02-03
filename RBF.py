import sys
inp_file = sys.argv[1]
commands = [  "[" , "]" , "<" , ">" , "+" , "-" , "." , "," ]
try:
    inp = open(inp_file,"r")
except:
    print("fatal error, file not found")
    exit()

m = inp.read()
c = []
for i in range(len(m)
):
    if m[i] in commands : c.append(m[i])
print(c)
