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

def main():
    prime = 2
    primes = [prime]
    wantAnother = True
    
    while wantAnother:
        print('Primes: {}'.format(primes))
        print('Do you want the next prime number? Y/N')
        answer = input('R: ').strip().upper()
        wantAnother = answer == 'Y'
        prime = nextPrime(prime)
        primes.append(prime)
    
    print('Program completed.')

if __name__ == '__main__':
    main()
