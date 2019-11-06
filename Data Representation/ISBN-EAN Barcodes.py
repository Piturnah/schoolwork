import random

_WEIGHT = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]

def Check_Code(code):
    if len(code) != 13:
        return False
    try:
        code = [ int(x) for x in code ]
    except:
        return False
    
    if Determine_Check_Digit(code) == code[-1]:
        return True
    else:
        return False

def Determine_Check_Digit(code):
    multiplied_list = []
    for i in range (0, 12):
        multiplied_list.append(code[i] * _WEIGHT[i])
    
    check_digit = sum(multiplied_list) % 10
    check_digit = 10 - check_digit
    if check_digit == 10:
        check_digit = 0
    return check_digit

def Generate_Barcode():
    barcode = []
    for i in range (0, 12):
        barcode.append(random.randint(0, 9))
        
    barcode.append(Determine_Check_Digit(list(barcode)))
    return "".join(map(str,barcode))
        
while True:
    selection = input ("\n1. Check barcode\n2. Generate barcode\n> ")
    if selection == "1":
        print("\n"+str(Check_Code(list(input()))))
    elif selection == "2":
        print("\n"+Generate_Barcode())
    input("Enter to continue\n> ")
