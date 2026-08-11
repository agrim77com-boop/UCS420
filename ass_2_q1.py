# 1
roll_no = 1024160088
L = [int(digit) * 10 for digit in str(roll_no)]
print("Initial list: ", L)

# 2 
L.append(150)
print("List after append(): ",L)
L.insert(2,200)
print("List after insert(): ",L)

#3
L.pop(2)
print("List after pop(): ",L)     #element at this index removed
L.remove(20)
print("List after remove(): ",L)  # first occurence of element removed

#4
L.sort()
print("List after sort(): ",L)
L.sort(reverse = True)
print("List after sort() {Descending}: ",L)

#5
print("First three elements:", L[:3])
print("Last three elements:", L[-3:]) 
print("Mid elements:", L[2:5])     #same as loop

#6
average = sum(L)/ len(L)
greater_than_average = [x for x in L if x > average]
print("Average: ",average)
print("Elements greater_than_average: ",greater_than_average)
