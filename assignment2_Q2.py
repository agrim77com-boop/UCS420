# 1
scores = (10, 0, 20, 40, 10, 60, 0, 0)   # tuple
highest = max(scores)
highest_index = scores.index(highest)
lowest = min(scores)
lowest_count = scores.count(lowest)

print("Scores:", scores)
print("Highest score:", highest)
print("Index of highest score:", highest_index)
print("Lowest score:", lowest)
print("Number of times lowest appears:", lowest_count)

# 2
rev = list(reversed(scores))
print("List after reversed: ",rev)

#3
user_score = int(input("Enter score:"))
if user_score in scores:
   print("First occurrence index:", scores.index(user_score))
else:
    print("Score is not present")
    
# 4
# scores[0] = 100
# This raises TypeError because tuples are immutable,
# while list elements can be changed after creation.

# 5
first_score, second_score, *remaining_scores = scores

print("First score:", first_score)
print("Second score:", second_score)
print("Remaining scores:", remaining_scores)
