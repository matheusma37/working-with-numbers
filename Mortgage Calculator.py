import math

def inputValue(text):
    value = -1.0
    while value <= 0:
        try:
            value = float(input('Input a value (greater '+
                                'than zero) for {}: '
                                .format(text)
                                )
                          )
        except:
            print('Please input a valid value.')
    return value

def main():    
    mortgage = inputValue('mortgage')
    loan = inputValue('monthly interest in %')
    monthsToPay = math.ceil(inputValue('payment times'))

    total = mortgage + mortgage*(loan/100)
    monthlyPayments = total/monthsToPay
    loanPayed = math.ceil(mortgage*(loan/100)/monthlyPayments)
    
    print('Total to pay: {}.'.format(total))
    print('Monthly payment: {}.'.format(monthlyPayments))
    print('The loan will be payed with {} months.'.format(loanPayed))

if __name__ == '__main__':
    main()
