import sys
def moon_weight():
    print('Enter your Earth weight: ')
    weight = float(sys.stdin.readline())
    print('Enter yearly weight increase: ')
    increase = float(sys.stdin.readline())
    print('Enter the number of years: ')
    years = int(sys.stdin.readline())
    years = years + 1
    for year in range(1, years):
        weight = weight + increase
        moon_weight = weight * 0.165
        print('Year %s = %s' % (year, moon_weight))

moon_weight()
