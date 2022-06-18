import random
import time
import math

EPSILON = 0.000001

passes = 0

# Square Root using Exhaustive Enumeration
def sqrt_method_1(number):
    epsilon = 0.0001
    num_guesses = 0
    if number < 1:
        start = epsilon
    else:
        start = 1

    while abs(start**2 - number) >= epsilon:
        num_guesses += 1
        print(f'Number: {number}, Guess is: {start}, Guess Square is {start**2} and Guess Square minus Number is Less Than {epsilon}: {abs(start ** 2 - number) < epsilon}.')
        if start ** 2 > number:
            start -= epsilon
        else:
            start += epsilon
    
    if abs(start ** 2 - number < epsilon):
        return(start, num_guesses)
    else:
        return
  

# Square Root using Bisection Methods
def sqrt_method_2(number):
    epsilon = 0.0000001
    num_guesses, low = 0, 0
    high = max(1, number)

    mid = (high + low) / 2

    while abs(mid**2 - number) >= epsilon:
        num_guesses += 1
        # print(f'Guess: {num_guesses}, Low: {low}, High: {high}, Ans: {mid} and Condition: {abs(mid**2 - number) >= epsilon}')

        if mid**2 < number:
            low = mid
        else:
            high = mid
        mid = (low + high) / 2

    if abs(mid ** 2 - number < epsilon):
        return(mid, num_guesses)
    else:
        return


# Square Root using Heron Of Alexandria 
def heron_of_alexandria(number, sqrt_number=None):
    if sqrt_number == None:
        sqrt_number = EPSILON
    
    global passes 
    
    passes += 1
    
    # print(f'Iteration: {passes}: Number: {number}, Estimated Square Root: {sqrt_number}, Error is { number - pow(sqrt_number, 2)} and {abs(number - (sqrt_number ** 2)) <= EPSILON}.')

    if (abs(number - (sqrt_number ** 2))) <= EPSILON:
        return (sqrt_number, passes)

    else:
        return heron_of_alexandria(number, (sqrt_number +(number / sqrt_number)) / 2)

if __name__ == '__main__':

    no_of_decimals = list(range(5))
    numbers_list = []
    for n in range(10):
        numbers_list.append(random.random() * (10 ** random.choice(no_of_decimals)))
    print(numbers_list)

   # print(numbers)
    tic = time.process_time()
    for number in numbers_list:
        result = sqrt_method_1(number)
    toc = time.process_time()
    print(f'Total Time taken to find square root of {len(numbers_list)} number(s) is {toc - tic}.')
    
