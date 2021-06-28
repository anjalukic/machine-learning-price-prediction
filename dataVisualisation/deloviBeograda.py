import json
import matplotlib.pyplot as plt
import numpy


def plotIt(locations):
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 34, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]

    x = numpy.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, men_means, width, label='Men')
    rects2 = ax.bar(x + width / 2, women_means, width, label='Women')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()
    '''labels = []
    values = []
    for loc in locations:
        labels.append(loc['deoBeograda'])
        values.append(loc['brojNekretnina'])

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, values, width, label='Broj nekretnina')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Broj nekretnina')
    ax.set_title('Najzastupljeniji delovi Beograda po broju nekretnina')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)

    fig.tight_layout()

    plt.show()'''


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
