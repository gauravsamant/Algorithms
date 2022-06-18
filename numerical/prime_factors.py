import random
import time
import math
from timeit import timeit

def prime_factors(number):
    divisor = 2
    passes = 1
    factors = []
    a = 2
    for _ in range(number // 2):
        if number % a == 0:
            factors.append(a)
            number = number // a
        else:
            a += 1
    return factors

    # if number % 2 == 0:
    #     return number // 2

    # for num in range(divisor, number//2, 2):
    #     print(f'Iteration: {passes}: Number: {number}, Divisor: {num}.')
    #     passes += 1
    #     if (number % num == 0):
    #         return num
    
    # return False

if __name__ == '__main__':
    number = random.randint(2000, 100000000)
    tic = time.process_time()
    result = prime_factors(60)
    toc = time.process_time()
    # print(timeit('prime_factors(number)', globals=globals()))

    print(f'Factors of {number} are {result} and took {toc - tic} time to compute')
    # if type(result) == int:
    #     print(f'the Number {number} is not prime. And its lowest divisor is {result}.')

    # if type(result) == bool:
    #     print(f'the Number {number} is prime.')
