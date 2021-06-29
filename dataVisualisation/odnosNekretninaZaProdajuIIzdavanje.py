import json
import matplotlib.pyplot as plt

def plotIt(locationSaleAndSublet):
    labels = []
    valuesSale = []
    valuesSublet = []
    sale_std = []
    sublet_std = []
    for p in locationSaleAndSublet:
        labels.append(p)
        valuesSale.append(locationSaleAndSublet[p][0])
        valuesSublet.append(locationSaleAndSublet[p][1])
        sale_std.append(0)
        sublet_std.append(0)

    width = 0.7       # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    p1 = ax.bar(labels, valuesSale, width, yerr=sale_std, label='Prodaja', color='steelblue')
    p2 = ax.bar(labels, valuesSublet, width, yerr=sublet_std, bottom=valuesSale, label='Izdavanje', color='salmon')
    ax.bar_label(p1, label_type='center')
    ax.bar_label(p2, label_type='center')
    ax.bar_label(p2)

    ax.set_ylabel('Broj nekretnina')
    ax.set_title('Broj nekretnina za prodaju i izdavanje po gradovima')
    ax.legend()

    fig.tight_layout()
    #fig.autofmt_xdate()
    plt.savefig('BrojNekretninaZaProdajuIIzdavanje.png')
    plt.show()


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
    plotIt(locationSaleAndSublet)
