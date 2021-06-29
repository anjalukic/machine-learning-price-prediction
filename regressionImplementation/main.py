import tkinter as tk

window = tk.Tk()
window.title('Nekretnine')
window.geometry("500x200")
#Title
title = tk.Label(text="DODAVANJE OGLASA")
title.pack()
#dropdown for sale or subletting
frame = tk.Frame()
lblForSale = tk.Label(text='Izaberite opciju: ', master=frame)
lblForSale.pack(fill=tk.Y, side=tk.LEFT)
forSaleVar = tk.StringVar(frame)
forSale = ['Prodaja', 'Izdavanje']
forSaleVar.set(forSale[0]) # default value
forSaleDropdown = tk.OptionMenu(frame, forSaleVar, *forSale)
forSaleDropdown.pack(fill=tk.Y, side=tk.LEFT)
frame.pack(fill=tk.X)

#dropdown for house or apartment
frame = tk.Frame()
lblPropertyType = tk.Label(text='Izaberite tip nekretnine: ', master=frame)
lblPropertyType.pack(fill=tk.Y, side=tk.LEFT)
propertyTypeVar = tk.StringVar(frame)
propertyType = ['Kuca', 'Stan']
propertyTypeVar.set(propertyType[0]) # default value
propertyTypeDropdown = tk.OptionMenu(frame, propertyTypeVar, *propertyType)
propertyTypeDropdown.pack(fill=tk.Y, side=tk.LEFT)
frame.pack(fill=tk.X)

#dropdown for the location
frame = tk.Frame()
lblLocation = tk.Label(text='Izaberite lokaciju: ', master=frame)
lblLocation.pack(fill=tk.Y, side=tk.LEFT)
locationVar = tk.StringVar(frame)
locations = ['Vozdovac', 'Novi Beograd']
locationVar.set(locations[0]) # default value
locationDropdown = tk.OptionMenu(frame, locationVar, *locations)
locationDropdown.pack(fill=tk.Y, side=tk.LEFT)
frame.pack(fill=tk.X)

#text field for the square footage
frame = tk.Frame()
lblSqFootage = tk.Label(text='Unesite povrsinu nekretnine: ', master=frame)
lblSqFootage.pack(fill=tk.Y, side=tk.LEFT)
entrySqFootage = tk.Entry(master=frame)
entrySqFootage.pack(fill=tk.Y, side=tk.LEFT)
lblm2 = tk.Label(text=' m2', master=frame)
lblm2.pack(fill=tk.Y, side=tk.LEFT)
frame.pack(fill=tk.X)


#go button
frame = tk.Frame()
goButton = tk.Button(text="Izracunaj", width=25, height=5, master=frame)
goButton.pack(fill=tk.Y, side=tk.LEFT)
frame.pack(fill=tk.X)


window.mainloop()
