import pandas as pd
import matplotlib.pyplot as plt

# Chart 1: Bar chart for top passers
df1 = pd.read_csv('data/topPassers.csv')

df1['full_name'] = df1['FIRST_NAME'] + ' ' +df1['LAST_NAME']

plt.bar(df1['full_name'], df1['total_pass_td'])
plt.xlabel('Quaterback')
plt.ylabel('Total Passing Touchdowns')
plt.title('Top 10 Passing TDs')
plt.savefig('topPassersChart.png')
plt.show()