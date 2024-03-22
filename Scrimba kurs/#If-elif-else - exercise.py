print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

def to_fahr(cels):
    return cels*9/5+32

def operation(a, sign, b):
    if sign=="+":
        return a+b
    elif sign=="-":
        return a-b
    elif sign=="*":
        return a*b
    elif sign=="/":
        if b!=0:
            return a/b
        else:
            return "an error. Division by 0 is impossible"
    else:
        return "impossible to calculate due to an improper sign. Rerun the program and use the exact symbol"


choice=input("Do you want to do some arithmetics(1) or convert temperature(2)?\n")

if choice=="1":
    a=float(input("Provide first number: "))
    sign=input("Choose operation from the set: {+, -, *, /}: ")
    b=float(input("Provide second number: "))
    print(f"The result: {operation(a,sign,b)}.")

elif choice=="2":
    temp=float(input("Provide a temperature in Celsius' degrees: "))
    print(f"This temperature is equivalent to {to_fahr(temp)} F.")

else:
    print("Improper choice. Rerun the program.")