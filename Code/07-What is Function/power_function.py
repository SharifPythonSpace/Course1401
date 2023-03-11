# 1. get input parameters
# 2. set initial value for output
# 3. calculate power
# 4. print result

number = 4
power = 3

def our_power(number, power):
    counter = 0

    result = 1
    while counter != power:
        result = result * number
        counter = counter + 1

    print('this is our result for power calculation: ', result)

our_power(2,5)
