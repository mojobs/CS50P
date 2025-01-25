prompt = input("Prompt: ")
elements = prompt.split(" ")
num1 = float(elements[0])
num2 = float(elements[2])
if elements[1] == '+':
    print(num1+num2)
elif elements[1] == '/':
    print(num1/num2)
elif elements[1] == '*':
    print(num1*num2)
elif elements[1] == '-':
    print(num1-num2)
else:
    print("Operator not found")
