import json

import matplotlib.pyplot as plt
import numpy as np


def plotIt(locations):

    labels = []
    values = []
    for loc in locations:
        labels.append(loc['deoBeograda'])
        values.append(loc['brojNekretnina'])

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, values, width)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Broj nekretnina')
    ax.set_title('Najzastupljeniji delovi Beograda po broju nekretnina')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    ax.bar_label(rects1, padding=0)

    fig.tight_layout()
    fig.autofmt_xdate()
    plt.show()


with open('top10DelovaBeograda.json') as json_file:
    locations = json.load(json_file)
    print(locations)
    plotIt(locations)
    '''locationNames = {}
    for row in locations:
        if row['preciseLocation'] is not None and row['location'] == 'Beograd':
            if row['preciseLocation'] in locationNames:
                locationNames[row['preciseLocation']] = locationNames[row['preciseLocation']]+1
            else:
                locationNames[row['preciseLocation']] = 1
    print(locationNames)'''
