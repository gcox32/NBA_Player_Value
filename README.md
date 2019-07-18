<img src="assets/brand logo.png" width="100" height="100"></a>

# NBA

### Order of Execution

> In order to recreate the visualizations seen here, it's important that one re-runs the code in the correct order.
> The 3 webscraping notebooks pull the majority of our data and take approximately 4 minutes 15 seconds each to run.
> Critically, the player-level data-wrangling must be performed after the webscraping and before the EDA.
> My efforts then brought me to the NBA_functions notebook, but those function have been saved as a .py file for use in the EDA, so there is no need to run that code.

>> 1. Data Acquisition: this includes all webscraping and data wrangling
>>> team Webscrape.ipynb <br>
>>> per_game Webscrape.ipynb <br>
>>> per_100 Webscrape.ipynb <br>
>>> salary data.ipynb <br>
>>> shooting Webscrape.ipynb
>>> Player-level Data Wrangling.ipynb <br>
>> 2. Function definitions: lib/ holds the .py files where we've created a few tedious functions that will help with the LDA and EDA
>>> lib/NBA_functions.py
>>> lib/Compensation.py
>> 3. Preliminary LDA and EDA: cluster analysis allowed us to draw new insights about players, as did basic EDA and visualizations on the team-level for teams
>>> Team-level EDA.ipynb <br>
>>> Player-level LDA.ipynb <br>
>> 4. Salary EDA: only after these first steps can we explore salary trends and the information that general managers might find most enticing
>>> Salary EDA.ipynb 
