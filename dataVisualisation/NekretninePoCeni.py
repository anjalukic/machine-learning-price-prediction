import json
import matplotlib.pyplot as plt

def plotIt(priceRange):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = []
    sizes = []
    explode = []
    sumTotal = 0
    for p in priceRange:
        sumTotal+=priceRange[p][0]
        labels.append(p+' €')
        sizes.append(priceRange[p][0])
        explode.append(0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct=lambda p: '{:.1f}%({:.0f})'.format(p, (p/100)*sumTotal),
            shadow=False, startangle=90, colors=['salmon', 'skyblue', 'khaki', 'olivedrab', 'firebrick'])
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title('Broj nekretnina po cenovnom rangu')

    plt.savefig('NekretninePoCeni.png')
    plt.show()


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
    plotIt(priceRange)
