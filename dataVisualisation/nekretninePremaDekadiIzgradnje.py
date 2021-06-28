import json

with open('realestate.json') as json_file:
    locations = json.load(json_file)
    decadeOfBuilding = {"<1951": 0, "1951-1960": 0, "1961-1970": 0, "1971-1980": 0, "1981-1990": 0, "1991-2000": 0, "2001-2010": 0, "2011-2020": 0, ">2020": 0}
    for row in locations:
        if row['yearOfBuilding'] is not None:
            if row['yearOfBuilding'] < 1951:
                decadeOfBuilding["<1951"] = decadeOfBuilding["<1951"] + 1
            elif 1951 <= row['yearOfBuilding'] < 1961:
                decadeOfBuilding["1951-1960"] = decadeOfBuilding["1951-1960"] + 1
            elif 1961 <= row['yearOfBuilding'] < 1971:
                decadeOfBuilding["1961-1970"] = decadeOfBuilding["1961-1970"] + 1
            elif 1971 <= row['yearOfBuilding'] < 1981:
                decadeOfBuilding["1971-1980"] = decadeOfBuilding["1971-1980"] + 1
            elif 1981 <= row['yearOfBuilding'] < 1991:
                decadeOfBuilding["1981-1990"] = decadeOfBuilding["1981-1990"] + 1
            elif 1991 <= row['yearOfBuilding'] < 2001:
                decadeOfBuilding["1991-2000"] = decadeOfBuilding["1991-2000"] + 1
            elif 2001 <= row['yearOfBuilding'] < 2011:
                decadeOfBuilding["2001-2010"] = decadeOfBuilding["2001-2010"] + 1
            elif 2011 <= row['yearOfBuilding'] < 2021:
                decadeOfBuilding["2011-2020"] = decadeOfBuilding["2011-2020"] + 1
            else:
                decadeOfBuilding[">2020"] = decadeOfBuilding[">2020"] + 1
    print(decadeOfBuilding)
