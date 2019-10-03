<img src="assets/brand logo.png" width="100" height="100"></a>

# NBA Player Value

## Table of Contents

- [The Data](#the-data)
- [The Features](#the-features)
- [Conclusions](#conclusions)
- [Replicate](#replicate)

## The Data

Team dataset: <a href="https://www.basketball-reference.com/leagues/NBA_2019.html" target="_blank">**Team-level Data**</a>

First Player-level dataset: <a href="https://www.basketball-reference.com/leagues/NBA_2019_per_poss.html" target="_blank">**Per 100 Possessions**</a>

Second Player-level dataset: <a href="https://www.basketball-reference.com/leagues/NBA_2019_advanced.html" target="_blank">**Advanced Stats**</a>

Third Player-level dataset: <a href="https://www.basketball-reference.com/players/c/cartevi01.html" target="_blank">**Shooting Stats (example)**</a>

## The Features

To list out every feature would be both tedious and overlooked 99 times out of 100, so look <a href="https://www.basketball-reference.com/players/c/cartevi01.html" target="_blank">**here**</a> for an example of the player profile from which we were drawing our features. For each player, stats were comprised of *per 100 possessions* stats, *advanced* stats, and *shooting* stats for every year they played. BeautifulSoup allowed us to pull data from the tables of interest.

If you don't plan on just zooming past and genuinely need a reference, here are the advanced stats in particular:

**PER** -- Player Efficiency Rating<br>
A measure of per-minute production standardized such that the league average is 15.<br>
**TS%** -- True Shooting Percentage<br>
A measure of shooting efficiency that takes into account 2-point field goals, 3-point field goals, and free throws.<br>
**3PAr** -- 3-Point Attempt Rate<br>
Percentage of FG Attempts from 3-Point Range<br>
**FTr** -- Free Throw Attempt Rate<br>
Number of FT Attempts Per FG Attempt<br>
**ORB%** -- Offensive Rebound Percentage<br>
An estimate of the percentage of available offensive rebounds a player grabbed while he was on the floor.<br>
**DRB%** -- Defensive Rebound Percentage<br>
An estimate of the percentage of available defensive rebounds a player grabbed while he was on the floor.<br>
**TRB%** -- Total Rebound Percentage<br>
An estimate of the percentage of available rebounds a player grabbed while he was on the floor.<br>
**AST%** -- Assist Percentage<br>
An estimate of the percentage of teammate field goals a player assisted while he was on the floor.<br>
**STL%** -- Steal Percentage<br>
An estimate of the percentage of opponent possessions that end with a steal by the player while he was on the floor.<br>
**BLK%** -- Block Percentage<br>
An estimate of the percentage of opponent two-point field goal attempts blocked by the player while he was on the floor.<br>
**TOV%** -- Turnover Percentage<br>
An estimate of turnovers committed per 100 plays.<br>
**USG%** -- Usage Percentage<br>
An estimate of the percentage of team plays used by a player while he was on the floor.<br>
**OWS** -- Offensive Win Shares<br>
An estimate of the number of wins contributed by a player due to his offense.<br>
**DWS** -- Defensive Win Shares<br>
An estimate of the number of wins contributed by a player due to his defense.<br>
**WS** -- Win Shares<br>
An estimate of the number of wins contributed by a player.<br>
**WS/48** -- Win Shares Per 48 Minutes<br>
An estimate of the number of wins contributed by a player per 48 minutes (league average is approximately .100)<br>
**OBPM** -- Offensive Box Plus/Minus<br>
A box score estimate of the offensive points per 100 possessions a player contributed above a league-average player, translated to an average team.<br>
**DBPM** -- Defensive Box Plus/Minus<br>
A box score estimate of the defensive points per 100 possessions a player contributed above a league-average player, translated to an average team.<br>
**BPM** -- Box Plus/Minus<br>
A box score estimate of the points per 100 possessions a player contributed above a league-average player, translated to an average team.<br>
**VORP** -- Value over Replacement Player<br>
A box score estimate of the points per 100 TEAM possessions that a player contributed above a replacement-level (-2.0) player, translated to an average team and prorated to an 82-game season. Multiply by 2.70 to convert to wins over replacement.<br>

## Conclusions

Our machine learning efforts culminated in a classifier analysis on the team-level and regression analysis on the player-level, predicting success and salaries respectively. Machine learning regression models have a hard time pinning down just what exactly gets a player paid. Because these models were able to rely on 30+ features and still had a difficult time predicting, we must conclude that we did not have the features that would predict salary well (i.e. they aren’t found on a stats sheet). Classifier models did not have the same trouble with predicting team success. Our models performed well at predicting whether a team would finish the season ranked in the top 4 based on things like how well the team show 3-pointers. Feature Importance between our salary regression and our team success classifier varied enough to raise flags—GMs aren’t using success predictors to determine player worth. The player that deserves to get paid (i.e. who is the most valuable) is the one who can shoot, both accurately and often.

## Replicate

This repository is primarily notebook files, but if you'd like to recreate, expound on, or better complete this project with .py files, feel free to reach out to me.