#starting by inputting the number you wish to test
number=int(input("input the number you wish to test  "))
x=0
y=1
count=0
#checking whether the number is a positive number or not
if number<=0 :
    print("please input a positive integer")
#if the number is positive then we go ahead and text it
else:
    while count<number:
        z=x+y
        #updating the integers through swapping
        x=y
        y=z
        count+=1
        #output
        if number==y:
            print(f"{number} is in the Fibonacci sequence.")
            break
        elif number==count:
            print(f"{number} does not belong to the Fibonacci sequence")
            break
        else:
            continue