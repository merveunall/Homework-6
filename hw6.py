# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
numbers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]
def CheckPrimeNumber(number):
    if int(number) in numbers:
        return "Number is Prime"
    else:
        return 'Number is not Prime'
def primeNumberList():
    return numbers
def transactionJustResult():
    result = []
    for i, n in enumerate(numbers):
        length = len(numbers)
        if (length == i + 1):
            print(result)
            break
        else:
            n1 = numbers[i]
            n2 = numbers[i + 1]
            result.append(n1*n2)


checkNumber = input(" 1- Give Number : ")
print(CheckPrimeNumber(checkNumber))
print('2 - Prime List : ')
print(primeNumberList())
print('3 - Result Fake Prime Numbers : ')
transactionJustResult()