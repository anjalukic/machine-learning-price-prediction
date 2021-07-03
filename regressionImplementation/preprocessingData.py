from geopy.distance import geodesic
import json

locations = {'Terazije':(44.8126696, 20.4612717), 'Savski Venac':(44.7821727, 20.4514425), 'Cukarica opstina':(44.68348839999999, 20.3850355),
             'Stari Grad opstina':(44.8184554, 20.4643411), 'Zvezdara opstina':(44.77671369999999, 20.5324028),
             'Vozdovac opstina':(44.7761819, 20.477074), 'Vracar':(44.7995311, 20.475025),'Palilula opstina':(44.9398868, 20.4626509),
            'Novi Beograd':(44.8099561, 20.380088), 'Rakovica opstina':(44.7189343, 20.4538059),'Zemun opstina':(44.85308879999999, 20.3686508),
             'Grocka opstina':(44.6705404, 20.7173705), 'Mladenovac opstina':(44.448105, 20.6980628),'Obrenovac opstina':(44.596795, 20.1242053),
            'Lazarevac opstina':(44.37881230000001, 20.2623661), 'Barajevo opstina':(44.5789646, 20.4125613),
             'Sopot opstina':(44.5218165, 20.5744258), 'Surcin opstina':(44.7541378, 20.2116933)}

distance = {}
for l in locations:
    distance[l] = geodesic(locations[l], locations['Terazije']).km
    #print(l)
    #print(geodesic(locations[l], locations['Terazije']))

print(distance)
with open('locationsInBelgrade.json', 'w') as outfile:
    json.dump(distance, outfile, indent=4)

preprocessedData = []

with open('realestateBelgrade.json') as json_file:
    realestate = json.load(json_file)
    # print(realestate)
    for r in realestate:
        row = {}
        row['price'] = r['price']
        row['distance'] = round(distance[r['preciseLocation']], 5)
        row['squareFootage'] = r['squareFootage']
        row['numberOfRooms'] = r['numberOfRooms']
        preprocessedData.append(row)
        # print(row)

print(len(preprocessedData))
with open('preprocessedRealestate.json', 'w') as outfile:
    json.dump(preprocessedData, outfile, indent=4)
