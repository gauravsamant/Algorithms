def harmonic_sum_rec(number):
    if number == 1:
        return 1
    else:
        return (1/number) + harmonic_sum_rec(number - 1)

def harmonic_sum_loop(number):
    total = 0
    for i in range(1, number+1):
        total += (1/i)
    return total


print(f'The Harmonic sum of 999 is {harmonic_sum_rec(999)} by using recussion.')
print(f'The Harmonic sum of 999 is {harmonic_sum_loop(999)} by using for loop.')