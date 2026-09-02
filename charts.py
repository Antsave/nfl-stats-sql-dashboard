import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

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
plt.bar(df3['full_name'], df3['total_td'])
plt.xlabel('Player')
plt.ylabel('Total Touchdowns Yards')
plt.title('Top 10 Touchdown Scorers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('topTdScorersChart.png')
plt.show()

#Chart 4: Horizontal bar chart for most team wins
plt.figure()   

df4 = pd.read_csv('data/mostWins.csv')
plt.barh(df4['team'], df4['total_wins'])
plt.xlabel('Total Wins')
plt.ylabel('Team')
plt.title('Top 10 Teams with most wins')
plt.tight_layout()
plt.savefig('mostWinsChart.png')
plt.show() 

#Chart 5: Horizontal bar chart for best team win percentage
plt.figure()   

df5 = pd.read_csv('data/bestWinPercentage.csv')
df5 ['win_percentage'] = df5['total_wins']/df5['total_games']
plt.barh(df5['team'], df5['win_percentage'])
plt.xlabel('Win Percentage')
plt.ylabel('Team')
plt.title('Top 10 Teams with the best win percentage')
plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
plt.tight_layout()
plt.savefig('bestWinPercentageChart.png')
plt.show() 

#Chart 6: Line chart for most passing seasons
plt.figure()   

df6 = pd.read_csv('data/topPassingYears.csv')
df6 = df6.sort_values('YEAR')
plt.plot(df6['YEAR'], df6['total_pass_yards'])
plt.xlabel('Year')
plt.ylabel('Passing yards')
plt.title('Best Passing Seasons')
plt.tight_layout()
plt.savefig('topPassingYearsChart.png')
plt.show() 

plt.figure()

df9 = pd.read_csv('data/teamTotalOffenseVsWinPct.csv')

plt.scatter(df9['total_offense_yards'], df9['win_percentage'])
plt.xlabel('Total Offensive Yards (Passing + Rushing)')
plt.ylabel('Win Percentage')
plt.title('Does a Dominant Offense Predict Winning?')
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.tight_layout()
for i in range(len(df9)):
    plt.annotate(df9['team'][i], (df9['total_offense_yards'][i], df9['win_percentage'][i]), fontsize=8)
plt.savefig('offenseVsWinPctChart.png')
plt.show()