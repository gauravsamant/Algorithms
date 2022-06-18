import random
import time

# define a function which takes a number and return root**pwr==number,
# if no such combination occur for root and pwr return false
# 1 < pwr < 6
def root_and_pwr(number):
    for root in range(1, number//2):
        for pwr in range(1, 6):
            if root ** pwr == number:
                return (number, root, pwr)
            if root ** pwr > number:
                break
    return False

if __name__ == '__main__':
    # number = random.randint(2, 10000)
    number = 27
    tic = time.process_time()
    result = root_and_pwr(number)
    toc = time.process_time()

    if type(result) == tuple:
        print(f'the Number {result[0]}  can be replaced as {result[1]} ** {result[2]} = {result[1] ** result[2]}.')

    if type(result) == bool:
        print(f'there is no combination such that X ^ Y == {number}.')
    