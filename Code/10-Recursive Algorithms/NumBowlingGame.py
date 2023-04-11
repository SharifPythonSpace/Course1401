# this is a nested function

"""
fksdjflkjg
lkdlksgjlkdjgljg
lkldglkdjg

"""
def f():
    """
    fdklgjlkdjfg
    lksjglkjdflgk
    """
    a = 1
    a = a * 2
    def g(a):
        a = a * 1.2
        return a
    result = g(a)
    return result

myvar = f()

# print(myvar)


# we want to design and implement a code
# for finding the number of total pins in bowling game
def findingPinsNumber(row_index):
    # num = 0
    # for i in range(1, row_index+1):
    #     num = num + i
    # return num

    if row_index == 1:
        return 1
    
    else:
        return row_index + findingPinsNumber(row_index -1)


print(findingPinsNumber(4))
