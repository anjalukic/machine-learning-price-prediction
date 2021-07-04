import json
import math
import tkinter as tk


with open('locationsInBelgrade.json') as json_file:
    locations = json.load(json_file)


with open('preprocessedRealestate.json') as json_file:
    data = json.load(json_file)

# preprocess the data - classify the prices to price range
for row in data:
    if row['price'] < 50000:
        row['price'] = 0
    elif 50000 <= row['price'] < 100000:
        row['price'] = 1
    elif 100000 <= row['price'] < 150000:
        row['price'] = 2
    elif 150000 <= row['price'] < 200000:
        row['price'] = 3
    else:
        row['price'] = 4

# find optimal k
k = int(round(math.sqrt(len(data)), 0))
if k % 2 == 0:
    k += 1
# print('k = '+str(k))


def takeSecond(elem):
    return elem[1]


def predictPrice(newData, useEuclid, hyperK):
    # check if k is out of range
    if hyperK > len(data):
        hyperK = len(data)
    distances = []
    # calculate distance for every piece of data
    for ind, row in enumerate(data):
        if useEuclid:
            distance = euclidDistance3Dim(row['distance'], newData[0], row['squareFootage'], newData[1], row['numberOfRooms'], newData[2])
        else:
            distance = manhattanDistance3Dim(row['distance'], newData[0], row['squareFootage'], newData[1], row['numberOfRooms'], newData[2])
        distances.append((ind, distance))
    # sort the distances
    distances.sort(key=takeSecond)
    priceRangeCounter = [0, 0, 0, 0, 0]
    # count all classes to find the most frequent
    for i in range(hyperK):
        priceRangeCounter[(data[distances[i][0]])['price']] += 1
    predictedPriceRange = priceRangeCounter.index(max(priceRangeCounter))
    return predictedPriceRange


def writePriceRange(rangeClass):
    if rangeClass == 0:
        return "Vasa nekretnina je procenjena na cenu ispod 50 000 evra."
    elif rangeClass == 1:
        return "Vasa nekretnina je procenjena na cenu izmedju 50 000 i 100 000 evra."
    elif rangeClass == 2:
        return "Vasa nekretnina je procenjena na cenu izmedju 100 000 i 150 000 evra."
    elif rangeClass == 3:
        return "Vasa nekretnina je procenjena na cenu izmedju 150 000 i 200 000 evra."
    else:
        return "Vasa nekretnina je procenjena na cenu preko 200 000 evra."


def euclidDistance3Dim(x1, x2, y1, y2, z1, z2):
    return math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2 + (z1-z2) ** 2)


def manhattanDistance3Dim(x1, x2, y1, y2, z1, z2):
    return abs(x1-x2) + abs(y1-y2) + abs(z1-z2)


def is_float(n):
    try:
        float_n = float(n)
    except ValueError:
        return False
    else:
        return True


def is_int(n):
    try:
        int_n = int(n)
    except ValueError:
        return False
    else:
        return True


window = tk.Tk()
window.title('Nekretnine')
window.geometry("400x300")
# Title
title = tk.Label(text="DODAVANJE OGLASA")
title.pack()

# dropdown for the location
frame = tk.Frame()
lblLocation = tk.Label(text='Izaberite lokaciju: ', master=frame)
lblLocation.pack(fill=tk.Y, side=tk.LEFT)
locationVar = tk.StringVar(frame)
locationList = list(locations.keys())
locationVar.set(locationList[0])  # default value
locationDropdown = tk.OptionMenu(frame, locationVar, *locationList)
locationDropdown.pack(fill=tk.Y, side=tk.LEFT)
frame.pack(fill=tk.X)

# text field for the square footage
frame = tk.Frame()
lblSqFootage = tk.Label(text='Unesite povrsinu nekretnine: ', master=frame)
lblSqFootage.pack(fill=tk.Y, side=tk.LEFT)
entrySqFootage = tk.Entry(master=frame)
entrySqFootage.pack(fill=tk.Y, side=tk.LEFT)
lblm2 = tk.Label(text=' m2', master=frame)
lblm2.pack(fill=tk.Y, side=tk.LEFT)
lblWarningSqFootage = tk.Label(text='', master=frame)
lblWarningSqFootage.pack(fill=tk.Y, side=tk.LEFT)
frame.pack(fill=tk.X)

# text field for the number of rooms
frame = tk.Frame()
lblNRooms = tk.Label(text='Unesite broj soba: ', master=frame)
lblNRooms.pack(fill=tk.Y, side=tk.LEFT)
entryNRooms = tk.Entry(master=frame)
entryNRooms.pack(fill=tk.Y, side=tk.LEFT)
lblWarningNRooms = tk.Label(text='', master=frame)
lblWarningNRooms.pack(fill=tk.Y, side=tk.LEFT)
frame.pack(fill=tk.X)

# estimated price label
labelFrame = tk.Frame()
lblPrice = tk.Label(text='', master=labelFrame)
lblPrice.pack(fill=tk.Y, side=tk.LEFT)

distanceTypes = {'Euklidovo rastojanje': True, 'Menhetnovo rastojanje': False}


def calculate():
    if entrySqFootage.get().isnumeric() and is_float(entryNRooms.get()):
        lblWarningSqFootage['text'] = ''
        lblWarningNRooms['text'] = ''
        priceRange = 0
        useEuclid = distanceTypes[distanceTypeVar.get()]
        if is_int(entryK.get()):
            priceRange = predictPrice([locations[locationVar.get()], int(entrySqFootage.get()), float(entryNRooms.get())], useEuclid, int(entryK.get()))
        else:
            priceRange = predictPrice([locations[locationVar.get()], int(entrySqFootage.get()), float(entryNRooms.get())], useEuclid, k)
        lblPrice['text'] = writePriceRange(priceRange)
    else:
        print('error in square footage or number of rooms')
        entrySqFootage.delete(0, tk.END)
        entryNRooms.delete(0, tk.END)
        lblWarningSqFootage['text'] = 'Unesite broj!'
        lblWarningNRooms['text'] = 'Unesite broj sa tackom za decimalni deo'

# go button
frame = tk.Frame()
goButton = tk.Button(text="Izracunaj", width=10, height=2, master=frame, command=calculate)
goButton.pack(fill=tk.Y, side=tk.LEFT)
frame.pack(fill=tk.X)
labelFrame.pack(fill=tk.X)

# model configuration
modelFrame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=2)
frame = tk.Frame(master=modelFrame)
title = tk.Label(text="Podesavanje modela za predikciju:", master = frame)
title.pack(fill=tk.Y, side=tk.LEFT)
frame.pack(fill=tk.X)
# text field for the k
frame = tk.Frame(master=modelFrame)
lblK = tk.Label(text='Unesite hiperparametar k za model: ', master=frame)
lblK.pack(fill=tk.Y, side=tk.LEFT)
entryK = tk.Entry(master=frame)
entryK.pack(fill=tk.Y, side=tk.LEFT)
frame.pack(fill=tk.X)
# dropdown for the location
frame = tk.Frame(master=modelFrame)
lblDistanceType = tk.Label(text='Izaberite tip rastojanja: ', master=frame)
lblDistanceType.pack(fill=tk.Y, side=tk.LEFT)
distanceTypeVar = tk.StringVar(frame)
distanceTypesList = list(distanceTypes.keys())
distanceTypeVar.set(distanceTypesList[0])  # default value
distanceTypeDropdown = tk.OptionMenu(frame, distanceTypeVar, *distanceTypesList)
distanceTypeDropdown.pack(fill=tk.Y, side=tk.LEFT)
frame.pack(fill=tk.X)
modelFrame.pack(fill=tk.X)

window.mainloop()








