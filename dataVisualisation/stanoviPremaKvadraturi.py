import json

import matplotlib.pyplot as plt
import numpy as np


def plotIt(squareFootage):

    labels = []
    values = []
    for property in squareFootage:
        labels.append(property+' m2')
        values.append(squareFootage[property])

    x = np.arange(len(labels))  # the label locations
    width = 0.6  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, values, width)
    i = 0
    for r in rects1:
        if i % 2 == 0:
            r.set_color('salmon')
        else:
            r.set_color('indianred')
        i += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Broj nekretnina')
    ax.set_title('Broj stanova u Srbiji za prodaju po kvadraturi')
    ax.set_xlabel('Kvadratura')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    ax.bar_label(rects1, padding=0)

    fig.tight_layout()
    fig.autofmt_xdate()
    plt.savefig('StanoviPremaKvadraturi.png')
    plt.show()



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
    plotIt(squareFootage)
