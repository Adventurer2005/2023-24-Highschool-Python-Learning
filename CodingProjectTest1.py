#get user data
input = input( ">> " )
#split data by spaces
parts = input.split(" ")
#assign variables
try:
    num1 = int(parts[0])
    num2 = int(parts[2])
except:
    print ("Error: Numbers must only contain digits.")
    quit()
op = parts[1]
if op == "+":
    solution = num1 + num2
elif op == "-":
    solution = num1 - num2
else:
    print ("Error: Operator must be '+' or '-'.")
    quit()
exp1 = 0
exp2 = 0
exp3 = 0

#give error codes if needed
if num1 >= 10**4 or num2 >= 10**4:
    print ("Error: Numbers cannot be more than four digits.")
else: 
    #find length of numbers
    loop = True
    while loop == True:
        if abs(num1) >= 10**exp1:
            exp1 = exp1 + 1
        if abs(num2) >= 10**exp2:
            exp2 = exp2 + 1
        else:
            loop = False
    
    while abs(solution) > 10**exp3:
        exp3 = exp3 + 1
    if exp1 > exp2:
        digit = exp1
    else:
        digit = exp2
    if num1 >= 0:
        nul1 = 1
    else:
        nul1 = 0
    if num2 >= 0:
        nul2 = 1
    else:
        nul2 = 0
    if solution >= 0:
        nul3 = 1
    else:
        nul3 = 0
    
    space1 = digit-exp1 + nul1
    space2 = digit-exp2 + nul2
    space3 = digit-exp3 + nul3
    line1 = " "
    for iter in range(space1):
        line1 = line1 + " "
    line1=line1+str(num1)
    line2 = op + ""
    for iter in range(space2):
        line2 = line2 + " "
    line2=line2+str(num2)
    line3 = "--"
    for iter in range(digit):
        line3 = line3 + "-"
    line4 = ""
    for iter in range(space3):
        line4 = line4 + " "
    line4 = line4+str(solution)
    output = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    print ( output )