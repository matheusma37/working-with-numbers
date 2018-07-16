if __name__ == '__main__':
    sequenceNumber = -1
    current = 1
    previous = 0;

    try:
        while sequenceNumber < 0:
            sequenceNumber = int(input('Enter a positive integer value: '))
    except:
        print('Error! Please input a integer value...')
        input()
        exit()

    print('Fibonacci\'s sequence for {} is: '.format(sequenceNumber))
    for value in range(sequenceNumber+1):
        print(previous, end=' ')
        auxiliar = current
        current += previous
        previous = auxiliar
