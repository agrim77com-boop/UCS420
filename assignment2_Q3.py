# 1
import random
random.seed(1024160088)
numbers = [random.randint(100, 900) for _ in range(10)] # 10 random values

print("Random numbers:",numbers)

# 2
odd = [x for x in numbers if x % 2 != 0]

print("Odd numbers:",odd)
print("Count of odd numbers:", len(odd))

# 3
even = [x for x in numbers if x % 2 == 0]

print("Even numbers:",even)
print("Count of even numbers:", len(even))

# 4
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# Create list of prime numbers
prime_numbers = [x for x in numbers if is_prime(x)]

print("Prime numbers:",prime_numbers)
print("Count of prime numbers:", len(prime_numbers))

# 5
most_freq = max(numbers , key = numbers.count)

print("Most frequent number:", most_freq)
print("Number of times it occurs:", numbers.count(most_freq))
