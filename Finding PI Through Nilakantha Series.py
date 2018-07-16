PI = 3
signalExchanger = 1
divider = 2

try:
    precision = int(input('''Enter the precision for the calculation.
The higher the input value, the closer to PI will be the result.
Input: '''))
    if precision < 1:
        raise ValueError
except:
    print('Error! Please input a positive integer value higher than zero...')
    input()
    exit()

for x in range(1, precision+1):
    PI += 4/(divider*(divider+1)*(divider+2)) * signalExchanger
    divider += 2
    signalExchanger *= -1

print('The result of PI is: {}'.format(PI))
