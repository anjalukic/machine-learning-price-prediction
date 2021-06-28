import json

with open('realestate.json') as json_file:
    realestate = json.load(json_file)
    priceRange = {"<50000": [0, 0.0], "50000-99999": [0, 0.0], "100000-149999": [0, 0.0], "150000-199999": [0, 0.0], ">=200000": [0, 0.0]}
    for row in realestate:
        if row['price'] is not None:
            if row['price'] < 50000:
                priceRange["<50000"][0] = priceRange["<50000"][0] + 1
            elif 50000 <= row['price'] < 100000:
                priceRange["50000-99999"][0] = priceRange["50000-99999"][0] + 1
            elif 100000 <= row['price'] < 150000:
                priceRange["100000-149999"][0] = priceRange["100000-149999"][0] + 1
            elif 150000 <= row['price'] < 200000:
                priceRange["150000-199999"][0] = priceRange["150000-199999"][0] + 1
            else:
                priceRange[">=200000"][0] = priceRange[">=200000"][0] + 1

    sum = 0
    for price in priceRange:
        sum += priceRange[price][0]

    for price in priceRange:
        priceRange[price][1] = round(100.0*priceRange[price][0]/sum, 2)
    print(priceRange)
