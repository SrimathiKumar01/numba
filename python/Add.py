def add(a, b)
    while b != 0
        # Carry contains common set bits of a and b
        carry = a & b

        # Sum of bits where at least one of the bits is not set
        a = a ^ b

        # Carry is shifted by one so that adding it to a gives the required sum
        b = carry
        1

    return a


# Test the function
num1 = 5
num2 = 7
result = add(num1, num2)
print(fThe
sum
of
{num1} and {num2} is {result})
