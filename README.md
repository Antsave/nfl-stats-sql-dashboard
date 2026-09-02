# Does a Dominant Offense Predict Wins? — An NFL Data Analysis

**Live dashboard:** [Tableau Public — Does a Dominant Offense Predict Wins?](https://public.tableau.com/app/profile/anthony.savage6846/viz/DoesaDominantOffensePredictWinsNFLAnalysis/Dashboard1)

## Why I built this

I wanted a project that used real relational data and actually answered a question, instead of just showing off a bunch of disconnected stats. The NFL has gotten more pass-heavy every year, so I figured: does that actually matter? Does throwing (or running) for more yards actually win you more games, or is that not really the point?

I used SQL to pull and shape the data, pandas to move it into CSVs, matplotlib to build the individual charts, and Tableau to put it all together into one dashboard.

## Short answer: not really

I expected some correlation. There isn't much of one.

- The Saints had the most total passing yards of any team in the dataset — and one of the worst win percentages (~43%).
- The Cowboys, Broncos, and 49ers, three of the top 5 teams by win rate, aren't anywhere near the top of the yardage leaderboard.
- The 49ers and Vikings both won at a 55%+ clip with some of the lowest total offensive output in the league.

Piling up yards doesn't seem to be what separates winning teams from losing ones. Efficiency and execution probably matter more than volume — which honestly makes sense once you think about it, but it's not what I expected going in.

## What's in this repo

```
NFL_Dashboard/
├── nfl.db                          # SQLite database — NFL games/players/stats since 2009
├── queries.py                      # All 9 SQL queries, exported to CSV via pandas
├── charts.py                       # Matplotlib charts (7 total)
├── data/                           # CSV outputs from queries.py
└── charts/                         # Saved chart images
```

## Tools

- **SQL (SQLite)** — joins, `UNION`, `HAVING`, subqueries, and CTEs (`WITH`)
- **Python / pandas** — turning query results into DataFrames, merging datasets, CSV exports
- **Matplotlib** — bar, horizontal bar, line, and an annotated scatter plot
- **Tableau Public** — the interactive dashboard tying everything together

## SQL stuff worth pointing out

- Joined `PLAYER_STATS → ROSTER → GAME` to connect individual stat lines to a specific season
- Used `UNION ALL` + a subquery to combine home and away results into one real win count per team (teams show up in two different columns depending on home/away, so this isn't a single simple `GROUP BY`)
- Used `HAVING` to filter out teams with too few games, so a small sample size couldn't fake a great win percentage
- Hit SQLite's integer-division bug the hard way (`wins / games` silently returns 0) and fixed it with `* 1.0`
- Used `WITH` (CTEs) to build two separate aggregations — team offense and team wins — then join them together in one query, which is the one that actually answers the question

## The 6 supporting charts

1. Top 10 Passers (career passing TDs)
2. Top 10 Rushers (career rushing yards)
3. Top 10 TD Scorers (all TD types combined)
4. Best Win Percentage by Team (min. 100 games)
5. League-Wide Passing Trend by Season
6. Total Offense vs. Win % — the chart that actually answers the question

## Data source

[nfl-database](https://github.com/bdetweiler/nfl-database) — games since 1970, detailed player stats since 2015.

## Running it yourself

```bash
git clone https://github.com/Antsave/nfl-stats-sql-dashboard.git
cd nfl-stats-sql-dashboard
pip install pandas matplotlib
python3 queries.py
python3 charts.py
```

---

Built by [Anthony Savage](https://www.linkedin.com/in/anthony-savage-758b5a2b7/) — mostly to get real practice with SQL and BI tools beyond what coursework covers.
