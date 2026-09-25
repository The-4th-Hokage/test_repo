def fizz_buzz(n):
    for elem in range(1, n):
        if (elem % 3 == 0) and (elem % 5 == 0):
            print('FizzBuzz')
        elif (elem % 5 == 0):
            print('Buzz')
        elif (elem % 3 == 0):
            print('Fizz')
        else: print(elem)


fizz_buzz(973)