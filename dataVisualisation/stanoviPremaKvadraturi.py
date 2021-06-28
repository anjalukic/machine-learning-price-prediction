import json

with open('realestate.json') as json_file:
    locations = json.load(json_file)
    squareFootage = {"<=35": 0, "36-50": 0, "51-65": 0, "66-80": 0, "81-95": 0, "96-110": 0, ">=111": 0}
    for row in locations:
        if row['forSale'] == 1 and row['propertyType'] == 1 and row['squareFootage'] is not None:
            if row['squareFootage'] <= 35:
                squareFootage["<=35"] = squareFootage["<=35"] + 1
            elif 35 < row['squareFootage'] < 51:
                squareFootage["36-50"] = squareFootage["36-50"] + 1
            elif 51 <= row['squareFootage'] < 66:
                squareFootage["51-65"] = squareFootage["51-65"] + 1
            elif 66 <= row['squareFootage'] < 81:
                squareFootage["66-80"] = squareFootage["66-80"] + 1
            elif 81 <= row['squareFootage'] < 96:
                squareFootage["81-95"] = squareFootage["81-95"] + 1
            elif 96 <= row['squareFootage'] < 111:
                squareFootage["96-110"] = squareFootage["96-110"] + 1
            else:
                squareFootage[">=111"] = squareFootage[">=111"] + 1
    print(squareFootage)
