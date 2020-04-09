# Largest palindrome product
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import time
start_time = time.process_time()

def get_largest_palindrom_product(count_of_digit):

    max_value = 10**count_of_digit
    largest_value = 0
    for i in range(max_value):
        for j in range(i,max_value):
            current_value = i * j
            if largest_value < current_value:
                if check_palindrom(current_value):
                    largest_value = current_value

    return largest_value

def check_palindrom(number):
    number = str(number)

    if len(number) % 2 != 0:
        return False

    half_len = int(len(number) / 2)
    for i in range(half_len):
        if number[i] != number[-(i+1)]:
            return False

    return True


lpp = get_largest_palindrom_product(3)
print(lpp)

end_time = time.process_time() - start_time
print("algorithm running time : ", end_time) # 0.140625 sec


