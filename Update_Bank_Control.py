# Code to update the Banorte movements from the outlook server and analyze them
from Functions import *
from Connection_to_Outlook import *
import pandas as pd
from openpyxl.workbook import Workbook

# account credentials
username = "email"
password = "password"

imap = Connect_to_Outlook(username, password)

# Look up emails from
Email_from = "notificacionesbanorte@banorte.com"
Subject = "Notificaciones Eventos por Cuenta (Cargo/Abono)"
Subject_2 = "Notificacion de Compra en Comercio"

# Create a dictionary to storage the information
Bank = {'Date': [], 'Movement': [], 'Subject': [], 'Amount': [], 'Balance': [], 'Account': []}

Old_data = pd.read_excel("Bank_data.xlsx", index_col=0)

# Set last balance
last_balance = Old_data['Balance'].iloc[len(Old_data)-1]

# Search for emails with subject "Notificaciones Eventos por Cuenta (Cargo/Abono)"
id_list, data = update_control(Old_data, Email_from, Subject, imap)

# Search for emails with subject "Notificacion de Compra en Comercio"
id_list_2, data_2 = update_control(Old_data, Email_from, Subject_2, imap)
print(id_list)
print(id_list_2)

# Function to extract the data of transfer movements
extract_data_from_Banorte_mails_1(id_list, Bank, imap)

# Function to extract the data of expenses in stores
extract_data_expenses_Banorte(id_list_2, Bank, imap)

# Creation of dataframe
Bank_Data = pd.DataFrame(Bank)

# Sort DataFrame by date
Bank_Data_by_date_real = Bank_Data.sort_values(by='Date')
new_index = range(len(Old_data), len(Old_data) + len(Bank_Data_by_date_real))
Bank_Data_by_date_real = Bank_Data_by_date_real.set_index(pd.Index(new_index), drop=True)

# Calculate balances
Update_Bank_data = calculate_new_balance(last_balance, Bank_Data_by_date_real)

# Set display options to show the entire DataFrame
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Print DataFrame
# print(Bank_Data_by_date_real)
print(Update_Bank_data)

# Append new movements to excel
update_data = pd.concat([Old_data, Update_Bank_data], ignore_index=False)
update_data.to_excel("Bank_data.xlsx", index=True)
