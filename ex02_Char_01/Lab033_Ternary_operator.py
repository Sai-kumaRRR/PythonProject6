#  if-else
# age> 18 -> watch a movie
# age <18 -> not allowed  to watch movie
# Ternary operator
# resulting_if_true if condition else result if_false
x = 5
y = 10
max_val = x if x> y else y
print(max_val)
age = input("enter your age\n")
age = int(age)
result = "yes" if age > 18 else "no"
print(result)
