import pandas as pd
import matplotlib.pyplot as plt

# Chart 1: Bar chart for top passers
df1 = pd.read_csv('data/topPassers.csv')

df1['full_name'] = df1['FIRST_NAME'] + ' ' +df1['LAST_NAME']

plt.bar(df1['full_name'], df1['total_pass_td'])
plt.xlabel('Quaterback')
plt.ylabel('Total Passing Touchdowns')
plt.title('Top 10 Passing TDs')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('topPassersChart.png')
plt.show()

#Chart 2: Bar chart for top rushers
plt.figure()   

df2 = pd.read_csv('data/topRushers.csv')
df2['full_name'] = df2['FIRST_NAME'] + ' ' + df2['LAST_NAME']
plt.bar(df2['full_name'], df2['total_rush_yd'])
plt.xlabel('Rusher')
plt.ylabel('Total Rushing Yards')
plt.title('Top 10 Rushers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('topRushersChart.png')
plt.show()

#Chart 3: Bar chart for top Touchdown Scorers
plt.figure()   

df3 = pd.read_csv('data/topTdScorers.csv')
df3['full_name'] = df3['FIRST_NAME'] + ' ' + df3['LAST_NAME']
plt.bar(df3['full_name'], df3['total_rush_yd'])
plt.xlabel('Player')
plt.ylabel('Total Touchdowns Yards')
plt.title('Top 10 Touchdown Scorers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('topTdScorersChart.png')
plt.show()

#Chart 4: Horizontal bar chart for most team wins
plt.figure()   

df3 = pd.read_csv('data/topTdScorers.csv')
df3['full_name'] = df3['FIRST_NAME'] + ' ' + df3['LAST_NAME']
plt.bar(df3['full_name'], df3['total_rush_yd'])
plt.xlabel('Player')
plt.ylabel('Total Touchdowns Yards')
plt.title('Top 10 Touchdown Scorers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('topTdScorersChart.png')
plt.show()