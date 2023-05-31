# importing "random" for random operations
import random

# using random() to generate a random number
# between 0 and 1
print("A random number between 0 and 1 is : ", end="")
print(random.random())

# using seed() to seed a random number
random.seed(5)

# printing mapped random number
print("The mapped random number with 5 is : ", end="")
print(random.random())

# using seed() to seed different random number
random.seed(7)

# printing mapped random number
print("The mapped random number with 7 is : ", end="")
print(random.random())

# using seed() to seed to 5 again
random.seed(5)

# printing mapped random number
print("The mapped random number with 5 is : ", end="")
print(random.random())

# using seed() to seed to 7 again
random.seed(7)

# printing mapped random number
print("The mapped random number with 7 is : ", end="")
print(random.random())
