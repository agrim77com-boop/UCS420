# Original dictionary
my_dict = {
    "name": "Agrim Bhatt",
    "roll_no": "1024160088",
    "branch": "CSE",
    "age": 20,
    "city": "Ludhiana"
}

# 1
my_dict["location"] = my_dict.pop("city")

print("After renaming city:", my_dict)


# 2
my_dict["cgpa"] = 8.5

print("After adding CGPA:", my_dict)


# 3
my_dict["age"] = my_dict["age"] + 1

print("After increasing age:", my_dict)

# 4

dict_pop = my_dict.copy()
removed_value = dict_pop.pop("branch")

print("Using pop():", dict_pop)
print("Value returned by pop():", removed_value)

dict_del = my_dict.copy()
del dict_del["branch"]

print("Using del:", dict_del)

# 5
print("Key-value pairs:")

for key, value in my_dict.items():
    print(key, "→", value)

# 6

if "email" in my_dict:
    print("Email:", my_dict["email"])
else:
    print("Email is not present in the dictionary.")


# 7
friend_dict = {
    "name": "Rahul Sharma",
    "roll_no": "1024160099",
    "branch": "ECE",
    "age": 21,
    "city": "Chandigarh"
}

merged_dict = {**my_dict, **friend_dict}
print("Merged dictionary:", merged_dict)

# 8
string_values = {
    key: value
    for key, value in my_dict.items()
    if isinstance(value, str)
}

print("Only string values:", string_values)
