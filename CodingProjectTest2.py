input1 = input(">> ")
answer = False
parts = input1.split(" ")
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
left = str(num1)
right = str(num2)
down = str(solution)
if len(left) > 4 or len(right) > 4:
    print("Error: Numbers cannot be more than four digits.")
    quit()
if len(left) > len(right):
    digit = len(left)
else:
    digit = len(right)
space1 = digit-len(left)
space2 = digit-len(right)
space3 = digit-len(down)+2
line1 = "  "
for iter in range(space1):
    line1 = line1 + " "
line1 = line1 + left
line2 = op + " "
for iter in range (space2):
    line2 = line2 + " "
line2 = line2 + right
line3 = "--"
for iter in range(digit):
    line3 = line3 + "-"
if answer == True:
    line4 = ""
    for iter in range(space3):
        line4 = line4 + " "
    line4 = line4 + down
    output = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
else:
    output = line1 + "\n" + line2 + "\n" + line3
print(output)