digits = [1,0,2,4,1,6,0,0]

A = {digit * 7 for digit in digits}
B = {digit * 9 for digit in digits}

print("Set A:", A)
print("Set B:", B)

# 6
union = A.union(B)
print("Union: ",union)

# 7
intersection = A.intersection(B)
print("Intersection: ",intersection)

# 8
A_minus_B = A.difference(B)
B_minus_A = B.difference(A)

print("A - B:", A_minus_B)
print("B - A:", B_minus_A)

# 9
symmetric_diff = A.symmetric_difference(B)
print("Symmetric difference:", symmetric_diff)

# 10
print("Is A a subset of B?", A.issubset(B))       #to check for subset and superset
print("Is B a superset of A?", B.issuperset(A))

# 11
X = int(input("Enter a value to remove from A: "))
A.discard(X)

print("A after discard:", A)
