"""
Description:

Armstrong numbers are an N-digit natural number that is the sum of its digits raised to
powers of N. For example: 153 = 13 + 53 + 33.

It is a algorithm that finds as many as possible of these numbers within a user-defined range.
"""


# Function that checks a Armstrong numbers in user-defined range
def find_armstrong_numbers(lower: int, upper: int) -> list[int]:
    list = []
    # Loop that searches the given range for armstrong numbers
    for i in range(lower, upper + 1):
        number = i
        sum = 0
        n = len(str(i))
        # Here we separate each digit (from right to left),
        # raise to the "n" power and then sum the results for all digits
        while i != 0:
            digit = i % 10
            sum = sum + digit ** n  #
            i = i // 10
        # Final check. If the obtained sum is equal to the checked number,
        # it is added to the returned list
        if number == sum:
            list.append(number)
    return list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Welcome prompt
    print("\nArmstrong Numbers Finder v1.0\n")

    # Lower and upper bound of range from user
    lower = int(input("Please enter the lower limit: "))
    upper = int(input("Please enter the upper limit: "))
    print("\nSearch for Armstrong numbers in range {} to {}\n".format(lower, upper))

    # Checking the speed of the program
    import time
    start = time.perf_counter()

    result = find_armstrong_numbers(lower, upper)
    print("In the range {} to {} were found {} Armstrong number(s)".format(lower, upper, len(result)))
    print(result)

    # Display of program execution time
    elapsed = time.perf_counter() - start
    print("\nIt took {:.2f}s".format(elapsed))

"""
Result:

Armstrong Numbers Finder v1.0

Please enter the lower limit: 0
Please enter the upper limit: 10000000

Search for Armstrong numbers in range 0 to 10000000

In the range 0 to 10000000 were found 25 Armstrong number(s)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 
 54748, 92727, 93084, 548834, 1741725, 4210818, 9800817, 9926315]

It took 21.89s
"""