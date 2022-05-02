import random


# using list comprehension + randrange()
# to generate random number list
def r():
    result = [random.randrange(1, 100) for i in range(5)]
    return result


print(r())
