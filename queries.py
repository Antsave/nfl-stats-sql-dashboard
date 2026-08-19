import sqlite3
import pandas as pd

# Connect to the database (make sure nfl.db is in the same folder as this file)
conn = sqlite3.connect('nfl.db')
cur = conn.cursor()

# Query 1: Top 10 players by total passing touchdowns
query = '''
SELECT 
    PLAYER.FIRST_NAME, 
    PLAYER.LAST_NAME, 
    SUM(PLAYER_STATS.PASS_TD) AS total_pass_td
FROM PLAYER_STATS
JOIN PLAYER ON PLAYER_STATS.PLAYER_ID = PLAYER.PLAYER_ID
GROUP BY PLAYER.PLAYER_ID
ORDER BY total_pass_td DESC
LIMIT 10
'''

df1 = pd.read_sql_query(query, conn)

df1.to_csv('topPassers.csv', index=False)

print(df1)


# Query 2: Top 10 players by total rushing yards
query2 = '''
SELECT 
    PLAYER.FIRST_NAME,
    PLAYER.LAST_NAME,
    SUM(PLAYER_STATS.RUSH_YARDS) AS total_rush_yd
FROM PLAYER_STATS
JOIN PLAYER ON PLAYER_STATS.PLAYER_ID = PLAYER.PLAYER_ID
GROUP BY PLAYER.PLAYER_ID
ORDER BY total_rush_yd DESC
LIMIT 10
'''

df2 = pd.read_sql_query(query2, conn)

df2.to_csv('topRushers.csv', index=False)

print(df2)

# Query 3: Top 10 players by total touchdowns
query3 = '''
SELECT 
    PLAYER.FIRST_NAME,
    PLAYER.LAST_NAME,
    SUM(PLAYER_STATS.RUSH_TD) + SUM(PLAYER_STATS.PASS_TD) + SUM(PLAYER_STATS.RECEIVING_TD) AS total_td
FROM PLAYER_STATS
JOIN PLAYER ON PLAYER_STATS.PLAYER_ID = PLAYER.PLAYER_ID
GROUP BY PLAYER.PLAYER_ID
ORDER BY total_td DESC
LIMIT 10
'''

df3 = pd.read_sql_query(query3, conn)

df3.to_csv ('topTdScorers.csv', index=False)

print(df3)

#Query 4: Top 10 teams by wins 
query4 = '''
SELECT 
    team,
    COUNT(*) AS total_wins
FROM (
    SELECT HOME_TEAM AS team
    FROM GAME
    WHERE HOME_TEAM_RESULT = 'W'

    UNION ALL

    SELECT VISITING_TEAM AS team
    FROM GAME
    WHERE VISITING_TEAM_RESULT = 'W'
) AS all_wins
GROUP BY team
ORDER BY total_wins DESC
LIMIT 10
'''
df4 = pd.read_sql_query(query4, conn)

df4.to_csv('mostWins.csv', index =False)

print(df4)

# Query 5: top 10 teams by win percentage 
query5 = '''
SELECT 
    team,
    COUNT(*) AS total_games,
    SUM(CASE WHEN result = 'W' THEN 1 ELSE 0 END) AS total_wins
FROM (
    SELECT HOME_TEAM AS team, HOME_TEAM_RESULT AS result
    FROM GAME

    UNION ALL

    SELECT VISITING_TEAM AS team, VISITING_TEAM_RESULT AS result
    FROM GAME
) AS all_games
GROUP BY team
HAVING total_games >= 100
ORDER BY (total_wins * 1.0 / total_games) DESC 
LIMIT 10
'''
df5 = pd.read_sql_query(query5, conn)

df5.to_csv('bestWinPercentage.csv', index=False)

print(df5)

# Query 6: Top years for passing yards
query6 = '''
SELECT 
    GAME.YEAR,
    SUM(PLAYER_STATS.PASS_YARDS) AS total_pass_yards
FROM PLAYER_STATS
JOIN ROSTER ON PLAYER_STATS.ROSTER_ID = ROSTER.ROSTER_ID
JOIN GAME ON ROSTER.GAME_ID = GAME.GAME_ID
GROUP BY GAME.YEAR
ORDER BY total_pass_yards DESC
'''

df6 = pd.read_sql_query(query6, conn)

df6.to_csv('topPassingYears.csv', index=False)

print(df6)

conn.close()

