import tkinter as tk
import json


with open('locationsInBelgrade.json') as json_file:
    locations = json.load(json_file)
# print(locations)

with open('modelParameters.json') as json_file:
    parameters = json.load(json_file)

with open('normalizationData.json') as json_file:
    normData = json.load(json_file)

def calculatePrice(location, squareFootage, numberOfRooms):
    normLocation = (locations[location]-normData[0][0])/(normData[0][1]-normData[0][0])
    normSquareFootage = (squareFootage - normData[1][0]) / (normData[1][1] - normData[1][0])
    normNumberOfRooms = (numberOfRooms - normData[2][0]) / (normData[2][1] - normData[2][0])
    hypothesis = parameters[0]+parameters[1]*normLocation+parameters[2]*normSquareFootage+parameters[3]*normNumberOfRooms
    return int(round(hypothesis, 0))


def is_float(n):
    try:
        float_n = float(n)
    except ValueError:
        return False
    else:
        return True


window = tk.Tk()
window.title('Nekretnine')
window.geometry("500x200")
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

def calculate():
    if entrySqFootage.get().isnumeric() and is_float(entryNRooms.get()):
        lblWarningSqFootage['text'] = ''
        lblWarningNRooms['text'] = ''
        # do something with the data
        lblPrice['text'] = 'Procenjena cena za Vasu nekretninu je '+str(calculatePrice(locationVar.get(), int(entrySqFootage.get()), float(entryNRooms.get()))) + ' eura.'
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


window.mainloop()
