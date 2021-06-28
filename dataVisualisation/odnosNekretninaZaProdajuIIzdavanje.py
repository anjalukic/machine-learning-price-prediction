import json

with open('realestate.json') as json_file:
    realestate = json.load(json_file)
    locationNames = {}
    for row in realestate:
        if row['location'] is not None:
            if row['location'] in locationNames:
                locationNames[row['location']] = locationNames[row['location']] + 1
            else:
                locationNames[row['location']] = 1
    sortedLocations = sorted(locationNames.items(), key=lambda x: x[1], reverse=True)
    sortedLocations = sortedLocations[:5]

    locationSaleAndSublet = {}
    for l in sortedLocations:
        locationSaleAndSublet[l[0]] = [0, 0, 0.0, 0.0]

    for row in realestate:
        if row['location'] is not None and row['location'] in locationSaleAndSublet.keys():
            if row['forSale'] == 1:
                locationSaleAndSublet[row['location']][0] += 1
            else:
                locationSaleAndSublet[row['location']][1] += 1

    for location in locationSaleAndSublet:
        locationSaleAndSublet[location][2] = round(100.0*locationSaleAndSublet[location][0]/(locationSaleAndSublet[location][0]+locationSaleAndSublet[location][1]),2)
        locationSaleAndSublet[location][3] = round(100.0 * locationSaleAndSublet[location][1] / (locationSaleAndSublet[location][0] + locationSaleAndSublet[location][1]),2)
    print(locationSaleAndSublet)
