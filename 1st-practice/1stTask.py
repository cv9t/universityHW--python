def checkInput(a, b):
    if(type(a) != int or type(b) != int): 
        print("\nIncorrect Input")
        return False
    return True



print("Input the first number:")
a = int(input())
print("\nInput the second number:")
b = int(input())
sum = 0
count = 0
if(checkInput(a, b)):
    for i in range(a, b+1): 
        if(i % 3 == 0):
            sum+=i
            count+=1
    print(sum / count)