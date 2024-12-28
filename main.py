n = int(input("enter the number of terms: "))

firstnumber = 0
secondnumber = 1

if n <= 0:
    print("please enter a positive number!")
elif n == 1:
    print("fibonacci series up to 1 term: ")
    print(firstnumber)
else:
    print("Fibonacci series: ")
    print(firstnumber, secondnumber, end=" ")
    for _ in range(2, n):
        nextnumber = firstnumber + secondnumber
        print(nextnumber, end=" ")
        firstnumber = secondnumber
        secondnumber = nextnumber

