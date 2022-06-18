def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def sum_of_prime(number):
    total = 0
    for i in range(2, number):
        if is_prime(i):
            total += i
    
    return total

def sum_of_powers_map(list1, list2):
    total = 0
    for ind, val in enumerate(zip(list1, list2, map(lambda x, y: x**y, list1, list2))):
        total += val[2]
        print(f'Index: {ind}, List 1: {val[0]}, List 2: {val[1]}, {list1[ind]}^{list2[ind]} = {val[2]}, Total: {total}')
    print(total)

# def gen_key_code():
#     code = (lambda book, plain_text: (
#         {c: str(book.find(c)) for c in }
#     ))

def code_dictionary(book):
    code = {c: str(book.find(c)) for c in book}
    return code

# def codify(plain_text, cipher):
#     code = (lambda book, text: (
#         {c: str(book.find(c)) for c in plain_text and book in cipher}
#     ))
#     return code

codify = (lambda cipher, plain_text:(
    {
        c: str(cipher.find(c)) for c in plain_text
    }
))

encoder = (lambda code_key, plain_text:
            ''.join(['*' + code_key[c] for c in plain_text])[1:]
)

book_cipher = 'the quick brown fox jumps over the lazy dog'
text = 'no is no'

encrypt = (lambda book_cipher, text: 
            encoder(codify(book_cipher, text), text)
)


# print(sum_of_prime(6))
# sum_of_powers_map([1,2,3,4,5], [2,3,4,5,6])
# cd = code_dictionary('the quick brown fox jumps over the lazy dog')
# code = codify('no is no', cd)
# for c in code:
#     print(c)

code = encrypt(book_cipher, text)
print(code)
