#beginning by typing in an input
print("input a number you'd like to test")
number=int(input())
#number **= 0.5
for s in range(2,number):
    if number % s==0:
        print("The number you input is not prime")
        break
    else:
        print("The number you input is prime")
        break