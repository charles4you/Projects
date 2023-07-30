# This program will analyze the statistics in real time of the NFL in order to decide who is going to win each match
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup
from thefuzz import fuzz
from thefuzz import process
import lxml

# Assign url of data
url_passing = "https://www.nfl.com/stats/team-stats/"
url_rushing = "https://www.nfl.com/stats/team-stats/offense/rushing/2022/reg/all"
url_receiving = "https://www.nfl.com/stats/team-stats/offense/receiving/2022/reg/all"
url_scoring = "https://www.nfl.com/stats/team-stats/offense/scoring/2022/reg/all"

# Read the data from link
data_passing = pd.read_html(url_passing)
data_rushing = pd.read_html(url_rushing)

# Assign data of passing to dataframe
nfl_passing = data_passing[0]
nfl_passing = nfl_passing.sort_values(by='Team')
nfl_passing_df = pd.DataFrame(nfl_passing)
nfl_passing_df = nfl_passing_df.reset_index(drop=True)

# Assign data of rushing to dataframe
nfl_rushing = data_rushing[0]
nfl_rushing = nfl_rushing.sort_values(by="Team")
nfl_rushing_df = pd.DataFrame(nfl_rushing)
nfl_rushing_df = nfl_rushing_df.reset_index(drop=True)

# Names of Teams
teams = ['49ers', 'Bears', 'Bengals', 'Bills', 'Broncos', 'Browns', 'Buccaneers', 'Cardinals', 'Chargers', 'Chiefs', 'Colts', 'Commanders', 'Cowboys', 'Dolphins', 'Eagles', 'Falcons', 'Giants', 'Jaguars', 'Jets', 'Lions', 'Packers', 'Panthers', 'Patriots', 'Raiders', 'Rams', 'Ravens', 'Saints', 'Seahawks', 'Steelers', 'Texans', 'Titans', 'Vikings']

# Clean names in DataFrame
for team in teams:
    matches = process.extract(team, nfl_passing_df['Team'], limit = nfl_passing_df.shape[0])
    for potential_match in matches:
        if potential_match[1] >=80:
            nfl_passing_df.loc[nfl_passing_df['Team'] == potential_match[0], 'Team'] = team
            nfl_rushing_df.loc[nfl_rushing_df['Team'] == potential_match[0], 'Team'] = team

# Show DataFrame of Passing stats
print(nfl_passing_df)
print(nfl_rushing_df)

# Team that has the most TD
most_td_by_passing = nfl_passing_df.loc[nfl_passing_df['TD'].idxmax()]
print("The "+str(most_td_by_passing['Team'])+" is the team with the most Touchdowns by pass in the 2022 NFL season with a total of: " +str(most_td_by_passing['TD'])+".")

# Team that has the most Int
most_int = nfl_passing_df.loc[nfl_passing_df['INT'].idxmax()]
print("The "+str(most_int['Team'])+" is the team with the most interceptions in the 2022 NFL season with a total of: " +str(most_int['INT'])+".")

# Team with the most Completed attempts by passing
most_cmp = nfl_passing_df.loc[nfl_passing_df['Cmp'].idxmax()]
print("The "+str(most_cmp['Team'])+" is the team with the most completed attempts by passing in the 2022 NFL season with a total of: " +str(most_cmp['Cmp'])+" which represents the "+str(most_cmp['Cmp %'])+ "%.")

# Most effective team in completed passes
most_cmp_percentage = nfl_passing_df.loc[nfl_passing_df['Cmp %'].idxmax()]
print("The "+str(most_cmp_percentage['Team'])+" is the most effective team in completing passes in the 2022 NFL season with a total of: " +str(most_cmp_percentage['Cmp'])+" completed passes in "+str(most_cmp_percentage['Att'])+" attempts which represents the "+str(most_cmp_percentage['Cmp %'])+ "% of effectiveness.")

# Plot for most touchdowns in NFL 2022 by team
df_td = nfl_passing_df.sort_values('TD', ascending=False)

plt.figure(figsize=(9,6))
plt.bar('Team', 'TD', data=df_td)
plt.xlabel('NFL Teams', size=10)
plt.xticks(rotation=90)
plt.ylabel('Touchdowns', size=10)
plt.title('Passing touchdowns by team in NFL 2022 season ')
plt.show()

# Plot for most touchdowns in NFL 2022 by team
df_rs_td = nfl_rushing_df.sort_values('TD', ascending=False)

plt.figure(figsize=(9,6))
plt.bar('Team', 'TD', data=df_rs_td)
plt.xlabel('NFL Teams', size=10)
plt.xticks(rotation=90)
plt.ylabel('Touchdowns', size=10)
plt.title('Rushing touchdowns by team in NFL 2022 season ')
plt.show()
