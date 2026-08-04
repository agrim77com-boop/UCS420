n = int(input("Enter val: "))
total = 0
for i in range(1,n):
    if(i%7 == 0 and i % 9 == 0):
        total += i
        print(total,"is the sum of num div by 7 and 9 till",n)  
