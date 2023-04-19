import random
def generator(min,max,order,times):
    num=[]
    for i in range(times):
        temp=random.randint(min,max)
        while order == 0 and temp in num:
            temp=random.randint(min,max)
        num.append(temp)
    return num


minimum = int(input("Min. Value:"))
maximum = int(input("Max. Value:"))


if minimum > maximum:
    minimum,maximum=maximum,minimum


print("'1' for repeated;\n'0' for unique;")
order = int(input("Input : "))
times = int(input("Input the no. of random number: "))

if (maximum - minimum +1) < times and order == 0:
    print(f"Range is not enough to generate {times} random numbers")
    times = int(input("Input the no. of random number again: "))

print("The random numbers are : ",generator(minimum,maximum,order,times))
