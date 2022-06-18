# A floating point number is represented as e.g. 1.919
# which is equal to 1919*10^(-3)
# It is represented it pair of significant digits and exponents
# i.e. 1.919 = 1919*10^(-3) = (1919, -3) [Pair of significant digits and exponents]
#  
# Let us assume we have to represent 0.625 as binary
# Now 0.625 = 625/1000 = 5/8 = 5 * 2^(-3)
# 5 is represented in binary as 101 and 3 is represented as 11
# Thus 5/8(base 10) = (101, -11)[base 2]

# Now how will we represent 0.1(base 10) in binary
# 0.1 = 1/10 = 1*10^(-1) = (1, -1) [Base 10]
# but when we convert 0.1 or 1/10 to binary
# 1 can be represented by 2^0, but 10 cannot be represented by any power of 2
#############################################################################
# so in binary representation 
# with 1 significant digit, the precision we can get is (1, -3) = 2^0/2^(-3)
# with 2 significant digit, 00, 01, 10, 11  => best precision we can get is [ 2^1 = 10 (base 2) / 2^4 = 1000 (base 2) ] = 2/16 = 0.125 
# so 2 is represented in binary as 10 and 4 is represented as 100, therefore, precision is (10, -100)
# similarly the best we can get with 4 significant digits is (0011, -101) = 3/32 or 0.09375
# With 5 significant digits (11001, -1000) = 25/256 = 0.09765625
# 
# There does not exist an integer SIG and EXP such that SIG * 2 ^ EXP = 0.1
# 
# 
# Python use 53 bits of precision for Floating Point Numbers
# significant digits stored for the
# Therefore, decimal number 0.1 will be
# 11001100110011001100110011001100110011001100110011001 with 53 significant digits in binary representation
# This is equivalent to the decimal number
# 0.1000000000000000055511151231257827021181583404541015625 

x = 0.0

for _ in range(10):
    x = x + 0.1
if x == 1.0:
    print(f'{x} is 1.0')
else:
    print(f'{x} is not 1.0')
    print(f'10 X 0.1 = 1 is {10 * 0.1 == x}')