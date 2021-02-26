def checkInput(number): 
    if(type(number) != int):
        return False

    return True

def fib(number):
    n0 = 0
    count = 0
    n1 = 1

    while(n1 <= number):
        n0, n1= n1, n1+n0
        count += 1

    if(n0 == number):
        return count

    return -1


print("Input the number:")
number = int(input())

if(checkInput(number)):
    print(fib(number))
else: 
    print("Incorrect input")