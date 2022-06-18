import random
import time
import math


def prime(number):
    divisor = 3
    passes = 1

    if number % 2 == 0:
        return number // 2

    for num in range(divisor, number//2, 2):
        print(f'Iteration: {passes}: Number: {number}, Divisor: {num}.')
        passes += 1
        if (number % num == 0):
            return num
    
    return False

if __name__ == '__main__':
    number = random.randint(2, 1000000)
    tic = time.process_time()
    result = prime(number)
    toc = time.process_time()

    if type(result) == int:
        print(f'the Number {number} is not prime. And its lowest divisor is {result}.')

    if type(result) == bool:
        print(f'the Number {number} is prime.')

    
