def checkInput(a, b):
    if(len(str(a)) == 4 and len((str(b))) == 4):
        return True
        
    return False


print("Input the numbers")

try:
    a, b = input().split()
    a, b = int(a), int(b)
    
except ValueError:
        print("Incorrect input")

else: 
    if(checkInput(a, b)):
        bulls = 0
        cows = 0
        a, b = str(a), str(b)

        for i in range (len(str(a))):
            for j in range (len(str(b))):

                if(a[i] == b[j]):
                    if(i == j): 
                        bulls += 1
                    else:
                        cows += 1
        
        print("%s %s" %(bulls, cows))
    else: 
        print("Incorrect input")