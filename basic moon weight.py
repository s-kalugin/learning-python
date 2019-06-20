def moon_weight(weight, increase):
    for year in range(1, 16):
        weight = weight + increase
        moon_weight = weight * 0.165
        print('Year %s = %s' % (year, moon_weight))
moon_weight(70, 1)
