from functools import reduce

def hcf_method1(num1, num2):
    factors = []
    
    minimum = min(num1, num2)

    while minimum > 1:
        for factor in range(2, minimum):
            print(f'Factor: {factor}')
            if num1 % factor == 0 and num2 % factor == 0:
                print(f'Factor Found: {factor}')
                factors.append(factor)
                minimum = minimum // factor
                num1 = num1 // factor
                num2 = num2 // factor
                print(f'Minimum: {minimum}, Number1: {num1}, Number2: {num2}.')   
                break
            else:
                continue
    
    return factors

def factors(number):
    factors = []
    while number > 1:
        print(f'Number: {number}')

        for factor in range(2, number + 1):
            if number % factor == 0:
                print(f'Factor Found: {factor}')
                factors.append(factor)
                number = number // factor
                break
            else:
                continue
    return factors

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

if __name__ == '__main__':
    number_list_org = [19]
    number_org = reduce(lambda x, y: x*y, number_list_org)
    print(f'Original Number: {number_org}')
    print(f'Original Factors: {number_list_org}')
    result = factors(number_org)
    print(f'Number Returned: {reduce(lambda x, y: x*y, result)}')
    print(f'Factors Returned: {result}')