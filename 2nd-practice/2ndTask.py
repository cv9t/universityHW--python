def checkInput(string):
    for i in string:
        if(i == "<" or i == ">" or i == "-"):
            continue
        else: 
            return False

    return True



print("Input the string")
string = str(input())

if(checkInput(string)):
    count = 0

    for i in range(len(string)):
        if(string[i: i+5] == ">>-->" or string[i: i+5] == "<--<<"):
            count += 1

    print(count)
else: 
    print("Incorrect line")