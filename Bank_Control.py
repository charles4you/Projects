# Code to extract the Banorte movements from the outlook server and analyze them
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

# Search for emails with subject "Notificaciones Eventos por Cuenta (Cargo/Abono)"
id_list, data = Search_in_Outlook(Email_from, Subject, imap)

# Search for emails with subject "Notificacion de Compra en Comercio"
id_list_2, data_2 = Search_in_Outlook(Email_from, Subject_2, imap)

# Create a dictionary to storage the information
Bank = {'Date': [], 'Movement': [], 'Subject': [], 'Amount': [], 'Balance': [], 'Account': []}

# Function to extract the data of expenses in stores
extract_data_expenses_Banorte(id_list_2, Bank, imap)

# Function to extract the data of transfer movements
extract_data_from_Banorte_mails_1(id_list, Bank, imap)

# Creation of dataframe
Bank_Data = pd.DataFrame(Bank)

# Change data type of date
Bank_Data['Date'] = pd.to_datetime(Bank_Data['Date'])

# Sort DataFrame by date
Bank_Data_by_date_real = Bank_Data.sort_values(by='Date')
Bank_Data_by_date_real = Bank_Data_by_date_real.reset_index(drop=True)

# Set display options to show the entire DataFrame
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# DataFrame with real balance
Bank_Data_by_date_real = set_last_balance(Bank_Data_by_date_real)
Final_Data = calculate_balance(Bank_Data_by_date_real)

# Print DataFrame
print(Final_Data.dtypes)

balance_per_month = Final_Data.groupby(Final_Data['Date'].dt.month).agg(Average_balance=('Balance', 'mean'))

df = Final_Data.set_index('Date')
balance_evey_31 = df.groupby(pd.Grouper(freq='30D'))['Balance'].mean()
print(balance_per_month)
print(balance_evey_31)

Final_Data.to_excel("Bank_data_test.xlsx")
