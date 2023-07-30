from tkinter import *
from PIL import Image, ImageTk
import pandas as pd

# Crear raiz
raiz = Tk()
raiz.title("Expo Ingeniería - Industrial Works")
raiz.iconbitmap("cetys.ico")
raiz.geometry("1000x750")

# Crear frame
miframe = Frame(raiz, width=2000, height=1000)
miframe.pack()

# Crear buscador de texto
busqueda = Entry(miframe)
busqueda.grid(row=1, column=1, padx=10, pady=10, columnspan=1)

# Label de buscador
Searchlabel = Label(miframe, text="Ingresa el número de parte:")
Searchlabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

# Poner imagen de ALW
miImagen = Image.open("alw.png")
miImagen_resize = miImagen.resize((88, 24))
my_img = ImageTk.PhotoImage(miImagen_resize)
logo_alw = Label(miframe, image=my_img)
logo_alw.grid(row=0, column=5, sticky="e", padx=20, pady=10)

# Poner imagen de CETYS
cetysimg = Image.open("cetys.png")
cetysimg_resize = cetysimg.resize((52, 40))
my_img_2 = ImageTk.PhotoImage(cetysimg_resize)
logo_cetys = Label(miframe, image=my_img_2)
logo_cetys.grid(row=0, column=0, sticky="w", padx=20, pady=10)

# Poner titulo de Programa
titulo = Label(miframe, text="Architectural Lighting Works", font=("Times New Roman", 16))
titulo.grid(row=0, column=1, padx=10, pady=10, columnspan=3)

# Crear variable de str
part_no_str = StringVar()
quantity = StringVar()
location = StringVar()
unitary_cost = StringVar()
total_cost = StringVar()
description = "Visualizador de dibujo"


# Crear parametros de información de numero de parte
part_no = Entry(miframe, state="readonly", textvariable=part_no_str)
part_no.grid(row=3, column=1, padx=10, pady=10)

partlabel = Label(miframe, text="El número de parte a buscar es:")
partlabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

# Crear parametros de información cantidad
quantityentry = Entry(miframe, state="readonly", textvariable=quantity)
quantityentry.grid(row=4, column=1, padx=10, pady=10)

quantitylabel = Label(miframe, text="Cantidad de unidades disponibles:")
quantitylabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

# Crear parametros de información ubicacion
locationentry = Entry(miframe, state="readonly", textvariable=location)
locationentry.grid(row=5, column=1, padx=10, pady=10)

locationlabel = Label(miframe, text="Ubicación en almacen:")
locationlabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

# Crear parametros de información costo unitario
uncostentry = Entry(miframe, state="readonly", textvariable=unitary_cost)
uncostentry.grid(row=6, column=1, padx=10, pady=10)

uncostlabel = Label(miframe, text="Costo unitario de parte ($Dlls):")
uncostlabel.grid(row=6, column=0, sticky="e", padx=10, pady=10)

# Crear parametros de información costo unitario
costentry = Entry(miframe, state="readonly", textvariable=total_cost)
costentry.grid(row=7, column=1, padx=10, pady=10)

costlabel = Label(miframe, text="Costo total en almacén ($Dlls):")
costlabel.grid(row=7, column=0, sticky="e", padx=10, pady=10)

# Crear objeto para mostrar dibujo
path = "loading.png"
dibujo = Image.open(path)
dibujo_resize = dibujo.resize((600, 440))
my_img_3 = ImageTk.PhotoImage(dibujo_resize)
dibujo_final = Label(miframe, image=my_img_3)
dibujo_final.grid(row=1, column=4, padx=20, pady=10, columnspan=2, rowspan=7)

dibujolabel = Label(miframe, text=description)
dibujolabel.grid(row=8, column=5, sticky="w", padx=10, pady=10)

# Creación de fotos de dibujos
path_1 = "609-000824.png"
new_image = Image.open(path_1).resize((600, 440))
dibujo_824 = ImageTk.PhotoImage(new_image)

path_2 = "20-00141-04.png"
new_image_2 = Image.open(path_2).resize((600, 440))
dibujo_04 = ImageTk.PhotoImage(new_image_2)

path_3 = "609-000017.png"
new_image_3 = Image.open(path_3).resize((600, 440))
dibujo_017 = ImageTk.PhotoImage(new_image_3)

path_4 = "609-000029.png"
new_image_4 = Image.open(path_4).resize((600, 440))
dibujo_029 = ImageTk.PhotoImage(new_image_4)

path_5 = "609-000215.png"
new_image_5 = Image.open(path_5).resize((600, 440))
dibujo_215 = ImageTk.PhotoImage(new_image_5)

path_6 = "609-000236.png"
new_image_6 = Image.open(path_6).resize((600, 440))
dibujo_236 = ImageTk.PhotoImage(new_image_6)

path_7 = "609-000237.png"
new_image_7 = Image.open(path_7).resize((600, 440))
dibujo_237 = ImageTk.PhotoImage(new_image_7)

path_8 = "609-000420.png"
new_image_8 = Image.open(path_8).resize((600, 440))
dibujo_420 = ImageTk.PhotoImage(new_image_8)

path_9 = "609-000421.png"
new_image_9 = Image.open(path_9).resize((600, 440))
dibujo_421 = ImageTk.PhotoImage(new_image_9)

path_10 = "609-000422.png"
new_image_10 = Image.open(path_10).resize((600, 440))
dibujo_422 = ImageTk.PhotoImage(new_image_10)

path_11 = "609-000845.png"
new_image_11 = Image.open(path_11).resize((600, 440))
dibujo_845 = ImageTk.PhotoImage(new_image_11)

path_12 = "609-000887.png"
new_image_12 = Image.open(path_12).resize((600, 440))
dibujo_887 = ImageTk.PhotoImage(new_image_12)

path_13 = "609-000890.png"
new_image_13 = Image.open(path_13).resize((600, 440))
dibujo_890 = ImageTk.PhotoImage(new_image_13)

path_14 = "609-000891.png"
new_image_14 = Image.open(path_14).resize((600, 440))
dibujo_891 = ImageTk.PhotoImage(new_image_14)

path_15 = "609-000894.png"
new_image_15 = Image.open(path_15).resize((600, 440))
dibujo_894 = ImageTk.PhotoImage(new_image_15)

path_16 = "609-001100.png"
new_image_16 = Image.open(path_16).resize((600, 440))
dibujo_1100 = ImageTk.PhotoImage(new_image_16)

path_17 = "609-001109.png"
new_image_17 = Image.open(path_17).resize((600, 440))
dibujo_1109 = ImageTk.PhotoImage(new_image_17)

path_18 = "609-001155.png"
new_image_18 = Image.open(path_18).resize((600, 440))
dibujo_1155 = ImageTk.PhotoImage(new_image_18)

path_19 = "Dibujona.png"
new_image_19 = Image.open(path_19).resize((600, 440))
dibujo_na = ImageTk.PhotoImage(new_image_19)


def information():
    """ Extract information from Database """
    # Get data from Excel Files
    file_name = r"C:\Users\carle\Documents\ExpoIng\Numeros de parte_Almacen_Final.xlsx"
    main_data = pd.read_excel(file_name, sheet_name='Main')

    part_number = str(busqueda.get())
    # Search part number in dataframe
    resultado = main_data.loc[main_data['Part number'] == part_number]

    # Declare the variables of the search
    location_v = resultado['Location'].iloc[0]
    quantity_v = resultado['Quantity'].iloc[0]
    cost_v = resultado['Cost'].iloc[0]
    total_cost_v = resultado['Total cost'].iloc[0]

    part_no_str.set(str(part_number))
    quantity.set(str(quantity_v))
    location.set(str(location_v))
    unitary_cost.set(str(cost_v))
    total_cost.set(str(total_cost_v))

    if part_number == "609-000824":
        dibujo_final.configure(image=dibujo_824)

    elif part_number == "20-00141-04":
        dibujo_final.configure(image=dibujo_04)

    elif part_number == "609-000017":
        dibujo_final.configure(image=dibujo_017)

    elif part_number == "609-000029":
        dibujo_final.configure(image=dibujo_029)

    elif part_number == "609-000215":
        dibujo_final.configure(image=dibujo_215)

    elif part_number == "609-000236":
        dibujo_final.configure(image=dibujo_236)

    elif part_number == "609-000237":
        dibujo_final.configure(image=dibujo_237)

    elif part_number == "609-000420":
        dibujo_final.configure(image=dibujo_420)

    elif part_number == "609-000421":
        dibujo_final.configure(image=dibujo_421)

    elif part_number == "609-000422":
        dibujo_final.configure(image=dibujo_422)

    elif part_number == "609-000845":
        dibujo_final.configure(image=dibujo_845)

    elif part_number == "609-000887":
        dibujo_final.configure(image=dibujo_887)

    elif part_number == "609-000890":
        dibujo_final.configure(image=dibujo_890)

    elif part_number == "609-000891":
        dibujo_final.configure(image=dibujo_891)

    elif part_number == "609-000894":
        dibujo_final.configure(image=dibujo_894)

    elif part_number == "609-001100":
        dibujo_final.configure(image=dibujo_1100)

    elif part_number == "609-001109":
        dibujo_final.configure(image=dibujo_1109)

    elif part_number == "609-001115":
        dibujo_final.configure(image=dibujo_1155)

    else:
        dibujo_final.configure(image=dibujo_na)


def limpiar():

    busqueda.delete(0, "end")
    part_no_str.set("")
    quantity.set("")
    location.set("")
    unitary_cost.set("")
    total_cost.set("")
    dibujo_final.configure(image=my_img_3)


# Crear Botón buscar
boton = Button(raiz, text="Buscar", command=information)
boton.pack(pady=5)

# Crear Botón limpiar
clean = Button(raiz, text="Limpiar", command=limpiar)
clean.pack(pady=5)


# Crear ciclo de raiz
raiz.mainloop()
