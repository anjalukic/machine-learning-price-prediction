import json
import matplotlib.pyplot as plt

def plotIt(parking):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = []
    sizes = []
    explode = []
    sumTotal = 0
    for p in parking:
        sumTotal+=parking[p]
        labels.append(p+' parking')
        sizes.append(parking[p])
        explode.append(0.02)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct=lambda p: '{:.1f}%({:.0f})'.format(p, (p/100)*sumTotal),
            shadow=False, startangle=90, colors=['salmon', 'skyblue'])
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title('Nekretnine sa parkingom')

    plt.savefig('NekretnineSaParkingom.png')
    plt.show()


with open('realestate.json') as json_file:
    realestate = json.load(json_file)
    parking = {"ima": 0, "nema": 0}
    for row in realestate:
        if row['location'] == 'Beograd':
            if row['parking'] is not None:
                parking['ima'] = parking['ima']+1
            else:
                parking['nema'] = parking['nema']+1

    print(parking)
    plotIt(parking)
