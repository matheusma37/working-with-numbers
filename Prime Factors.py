import math

def isPrime(value):
    for v in range(2, (value//2)+1):
        if value % v == 0:
            return False
    else:
        return True

def nextPrime(value):
    init = value+1
    while True:
        if isPrime(init):
            return init
        init += 1

if __name__ == '__main__':

    number = 0
    primal = 2
    primeFactors = []
    
    try:
        number = int(input('Input a number: '))
    except:
        print('It\'s not a number. Please enter with a number...')
        exit()
    
    number = math.fabs(number)
    
    if number < 2:
        print('There are no prime numbers for {}.'.format(int(number)))
        exit()

    while True:
        if number % primal == 0:
            primeFactors.append(primal)
            if number / primal == 1:
                break
            number /= primal
        else:
            primal = nextPrime(primal)

    print('Division by prime factors: ', primeFactors)
    print('Prime factors: ', set(primeFactors))
