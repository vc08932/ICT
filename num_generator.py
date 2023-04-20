import random
import sys

def generator(min,max,order,times):
    num=[]
    for i in range(times):
        temp=random.randint(min,max)
        while order == 0 and temp in num:
            temp=random.randint(min,max)
        num.append(temp)
    return num

while True:
    print("Input 'e' to exit the program.")

    minimum = input("Min. Value:").strip()
    
    if minimum.isnumeric() == False:
        print("Program is exit")
        sys.exit()
        
    minimum=int(minimum)
    maximum = int(input("Max. Value:"))


    if minimum > maximum:
        minimum,maximum=maximum,minimum


    print("'1' for repeated;\n'0' for unique;")
    order = int(input("Input : "))
    
    while order not in (0,1):
        print("Please input '0'/'1'")
        order = int(input("Input : "))

    times = int(input("Input the no. of random number: "))

    if (maximum - minimum +1) < times and order == 0:
        print(f"Range is not enough to generate {times} random numbers")
        times = int(input("Input the no. of random number again: "))

    output=generator(minimum,maximum,order,times)
    print("The random numbers are ",output,"\n","="*20,"\n")
