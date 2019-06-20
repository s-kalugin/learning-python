def moon_weight(weight, increase, years):
    years = years + 1
    for year in range(1, years):
        weight = weight + increase
        moon_weight = weight * 0.165
        print('Year %s = %s' % (year, moon_weight))

moon_weight(70, 0.8, 10)
