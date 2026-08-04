def sumPrime(n):
    total = 0

    for num in range(2, n + 1):
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            total += num

    return total


print("Sum of prime numbers:", sumPrime(10))
