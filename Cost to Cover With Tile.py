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
    floorHeight = inputValue('area height')
    floorWidth = inputValue('area width')

    tileHeight = inputValue('tile height')
    tileWidth = inputValue('area width')
    tileCost = inputValue('tile cost')

    tileArea = tileHeight * tileWidth
    floorArea = floorHeight * floorWidth

    totalCost = (floorArea/tileArea) * tileCost

    print('The total cost to cover the floor is $ {}.'
          .format(totalCost)
          )

if __name__ == '__main__':
    main()
