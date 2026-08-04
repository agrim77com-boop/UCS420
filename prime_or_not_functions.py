def prime(n):
  if(n <= 1):
    print("Not a prime")
  else :
    is_prime = True

    for i in range (2,n):
      if(n%i == 0):
        is_prime = False
        break
      
    if is_prime:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")

prime(2)
