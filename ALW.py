import pandas as pd

# Get data from Excel Files
File_name = r"/Users/admin/Documents/Ingeniería Industrial/ExpoIng/Numeros de parte_Almacen_Final.xlsx"
Main_data = pd.read_excel(File_name, sheet_name='Main')

print(Main_data.head())
# Type the part number
Busqueda = input("Numero de parte:")

# Search part number in dataframe
Resultado = Main_data.loc[Main_data['Part number'] == Busqueda]

# Declare the variables of the search
Part_number = Resultado['Part number'].iloc[0]
Location = Resultado['Location'].iloc[0]
Quantity = Resultado['Quantity'].iloc[0]
Cost = Resultado['Cost'].iloc[0]
Total_cost = Resultado['Total cost'].iloc[0]

print(Resultado)
print("The location of the part: " +Part_number+" is " +Location)
