# Laboratorio 2 - Modeling two variables
from numpy.random import choice
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data costumers
costumers = [8, 10, 12, 14]
probability_costumer = [0.35, 0.3, 0.25, 0.1]

# Data dozens
dozen_bought = [1, 2, 3, 4]
probability_dozen = [0.4, 0.3, 0.2, 0.1]

# Dictionaries
weekly_sales = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
weekly_costumers = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
weekly_dozens = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
recomendation = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
recomendation_not_compleating_demand = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
profit_compleating_demand = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
profit_not_compleating_demand = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
intervals = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
salvage_units_sd = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
income_dic = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
income_ns_dic = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
salvage_units_ns = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
lost_sales_dic = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}

dozen = []
np.random.seed(1)
for times in range(10):
    for weekday in weekly_sales.keys():
        # Select randomly amount of costumers
        random_number_costumer = choice(costumers, 1, p=probability_costumer)
        weekly_costumers[weekday].append(int(random_number_costumer))

        for i in range(int(random_number_costumer)):
            # Select Randomly amount of dozens
            random_number_dozen = choice(dozen_bought, 1, p=probability_dozen)
            dozen.append(random_number_dozen)
            dozen_sales_day = sum(dozen)

        # Multiply costumers and dozens
        weekly_sales[weekday].append(int(dozen_sales_day))
        weekly_dozens[weekday].append(dozen)
        dozen = [0]

# Create DataFrames
weekly_sales_df = pd.DataFrame(weekly_sales)
weekly_costumers_df = pd.DataFrame(weekly_costumers)
weekly_dozens_df = pd.DataFrame(weekly_dozens)

# Print Dataframes
print("Weekly customers per day")
print(weekly_costumers_df)
print("")
print("Weekly dozens per day")
print(weekly_dozens_df)
print("")
print("Weekly Sales per day")
print(weekly_sales_df)

# Calculate mean daily
# print("The mean of each day demand is")
# print(weekly_sales_df.mean())

print("The Rounded mean is:")
print(np.around(weekly_sales_df.mean()))

# Confidence intervals
for weekday in intervals.keys():
    point_estimate = weekly_sales_df[weekday].mean()
    std = np.std(weekly_sales_df[weekday])
    lower = point_estimate - std
    intervals[weekday].append(lower)
    upper = point_estimate + std
    intervals[weekday].append(upper)

# Recomendations to compleate demand
for weekday in recomendation.keys():
    multiple = weekly_sales_df[weekday].mean() / 5
    production = 5 * np.around(multiple)
    if production < weekly_sales_df[weekday].mean():
        production += 5
        recomendation[weekday].append(production)
    else:
        recomendation[weekday].append(production)

# Recomendation when not compleating demand
for weekday in recomendation_not_compleating_demand.keys():
    multiple_2 = weekly_sales_df[weekday].mean() / 5
    production = 5 * np.around(multiple_2)
    recomendation_not_compleating_demand[weekday].append(production)

# Create recomendation dataframe
recomendation_df = pd.DataFrame(recomendation)
recomendation_not_compleating_demand_df = pd.DataFrame(recomendation_not_compleating_demand)

# Print options of production
print("Production plan Scenario 1")
print(recomendation_df)
print("Production plan Scenario 2")
print(recomendation_not_compleating_demand_df)

# Analysis of profit while always compleating the demand
for weekday in profit_compleating_demand.keys():
    income = round(weekly_sales_df[weekday].mean()) * 8.4
    income_dic[weekday].append(income)
    manufacturing_cost = recomendation_df[weekday] * 5.8
    if int(recomendation_df[weekday]) > round(weekly_sales_df[weekday].mean()):
        salvage = (recomendation_df[weekday] - round(weekly_sales_df[weekday].mean())) * 4.20
        salvage_units_sd[weekday].append((recomendation_df[weekday] - round(weekly_sales_df[weekday].mean())))
        profit_value = income + salvage - manufacturing_cost
        profit_compleating_demand[weekday].append(int(profit_value))
    else:
        profit_value = income - manufacturing_cost
        profit_compleating_demand[weekday].append(int(profit_value))

# Analysis of profit when not compleating the demand
for weekday in profit_not_compleating_demand.keys():
    income_2 = round(weekly_sales_df[weekday].mean()) * 8.4
    income_ns_dic[weekday].append(income_2)
    manufacturing_cost_2 = recomendation_not_compleating_demand_df[weekday] * 5.8
    if round(weekly_sales_df[weekday].mean()) > int(recomendation_not_compleating_demand_df[weekday]):
        lost_sales = (round(weekly_sales_df[weekday].mean()) - recomendation_not_compleating_demand_df[weekday]) * 8.4
        lost_sales_dic[weekday].append((round(weekly_sales_df[weekday].mean()) - recomendation_not_compleating_demand_df[weekday]))
        profit_value_2 = income_2 - manufacturing_cost_2 - lost_sales
        profit_not_compleating_demand[weekday].append(float(profit_value_2))
        salvage_units_ns[weekday].append(0)
    else:
        salvage_2 = (recomendation_not_compleating_demand_df[weekday] - round(weekly_sales_df[weekday].mean())) * 4.20
        salvage_units_ns[weekday].append((recomendation_not_compleating_demand_df[weekday] - round(weekly_sales_df[weekday].mean())))
        profit_value_2 = income_2 + salvage_2 - manufacturing_cost_2
        profit_not_compleating_demand[weekday].append(float(profit_value_2))
        lost_sales_dic[weekday].append(0)

# Create profit dataframe
profit_df = pd.DataFrame(profit_compleating_demand)
profit_2_df = pd.DataFrame(profit_not_compleating_demand)
print("The profit each day while always compleating the demand will be of: ($Dlls)")
print(profit_df)
profit_scenario_1 = float(profit_df.sum(axis=1))
print("The total profit for scenario 1 is: " + str(profit_scenario_1))
print("The profit each day when not compleating the demand will be of: ($Dlls)")
print(profit_2_df)
profit_scenario_2 = float(profit_2_df.sum(axis=1))
print("The total profit for scenario 2 is: " + str(profit_scenario_2))

# Create income dataframe
income_ns_dic_df = pd.DataFrame(income_ns_dic)
salvage_units_ns_df = pd.DataFrame(salvage_units_ns)
lost_sales_df = pd.DataFrame(lost_sales_dic)
selection = ""
# Print recomendation
print("\n")
if profit_scenario_1 > profit_scenario_2:
    print("The company should produce each day (units) by always satisfying the demand")
    print(recomendation_df)
    selection = recomendation_df
    print("\n The total profit will be of ($): " + str(profit_scenario_1))
    print("Income: " + str(sum(income_dic)))
    print("Salvage: (" + str(sum(salvage_units_sd)) + ": unities) = " + str(sum(salvage_units_sd) * 4.2))
    print("Manufacturing costs: " + str(recomendation_df.sum() * 5.8))

else:
    print("The company should produce each day (units) by not always satisfying the demand")
    print(recomendation_not_compleating_demand_df)
    selection = recomendation_not_compleating_demand_df
    print("\nThe total profit will be of ($): " + str(profit_scenario_2))
    print(" Income: $" + str(int(income_ns_dic_df.sum(axis=1))))
    print(" Salvage: (" + str(int(salvage_units_ns_df.sum(axis=1))) + " unities) = " + "$" + str(int(salvage_units_ns_df.sum(axis=1)) * 4.2))
    print(" Lost Sales: (" + str(int(lost_sales_df.sum(axis=1))) + " unities) = " + "$" + str(int(lost_sales_df.sum(axis=1)) * 8.4))
    print(" Manufacturing costs: $" + str(int(recomendation_not_compleating_demand_df.sum(axis=1) * 5.8)))

# Confidence intervals DataFrame
intervals_df = pd.DataFrame(intervals)
intervals_df['Interval'] = ['Lower', 'Upper']
# Print confidence intervals
intervals_df = intervals_df.set_index('Interval')
print("\n The confidence intervals by day are: ")
print(intervals_df)

# Graphic histogram
plt.hist(weekly_costumers_df)
plt.xlabel('Number of customers')
plt.ylabel("Frequency of clients")
plt.legend(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
plt.title("Frequency of number of clients per day")
plt.show()

# Boxplot graphic
values = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
x = [1, 2, 3, 4, 5]
plt.boxplot(weekly_sales_df)
plt.xlabel("Day of the week")
plt.xticks(x, values)
plt.ylabel("Number of sold dozens")
plt.title("Weekly sales")
plt.show()
