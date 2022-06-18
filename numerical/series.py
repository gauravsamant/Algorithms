from functools import reduce

def fab(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    nth_term = fab(n - 1) + fab(n - 2)

    return nth_term

def sum_of_fab(n):
    total = 0

    fab_number = []

    for number in range(n):
        fab_number.append(fab(number))

    # print(fab_number)
    # total = reduce(lambda a, b: a + b, fab_number)
    total = sum(fab_number)
    return total

def accumulate(lis):
    modified_list = []

    # x = list(map(lambda x, y: x + y for x in lis and ( lambda y: 0 if lis[0] == x else )))
    # m_l = [lambda x , y: x + y, lis, list(lambda i, y: 0 if i == 0 else lis[i-1], list(lambda i: (i, _) in enumerate(lis)))]
    # m_l = 
    # print(m_l)
    for ind, ele in enumerate(lis):
        if ind == 0:
            print(f'index: {ind}')
            modified_list.append(ele)
        else:
            modified_list.append(modified_list[ind - 1] + ele)
    return modified_list


# print(fab(2))
# print(fab(5))
# print(sum_of_fab(10))
print(accumulate([1,3,4,10,4]))