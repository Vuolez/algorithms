# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def get_largest_prime_factor(number):
    prime_factors = []
    devider = 2
    currevnt_value = number
    while(True):

        if(currevnt_value == 1):
            return prime_factors

        if(currevnt_value % devider == 0):
            currevnt_value = currevnt_value / devider
            prime_factors.append(devider)
        else:
            devider += 1

lpf = get_prime_factor(600851475143)
print(lpf[-1])
