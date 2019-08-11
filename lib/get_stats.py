#!/usr/bin/env python
# coding: utf-8

# [Using Machine Learning to Find the 8 Types of Players in the NBA](https://fastbreakdata.com/classifying-the-modern-nba-player-with-machine-learning-539da03bb824 "fastbreakdata")

# Import necessary libraries

# In[1]:


import numpy as np
import warnings
warnings.simplefilter("ignore", UserWarning)

import pandas as pd


# ## 1.1 Data

# In[5]:


players = pd.read_csv('data/processed/players_final.csv')
# players = players.drop(columns = 'Unnamed: 0')

teams = pd.read_csv('data/processed/teams_final.csv')
teams = teams.drop(columns = 'Unnamed: 0')


# ### First function : 'get_stats'

# Our first function is going to be a real workhorse for us. Because we have 61 columns, we would need to be tediously slicing in order to ever look at the information we wanted. 'get_stats' will use .loc to slice as many or as few columns as needed, sort (and rank) by the first column given, and then return either a dataframe object or a prettier styled object based on the 'title' argument (False and True, respectively).

# In[7]:


def get_stats(*args, n = 10, team = 'all', position = 'all', 
              ascending = False, title = False, data = players):
    """slices nba df based on category, sorts descending and gives top n all-time or by year.
       Critically, the default 'title' setting of False will produce a pandas DataFrame object,
       while setting 'title' to True will produce a most visually appealing style object."""
    
    # create column headers with standard info and then append each stat category of interest
    col_list = ['Last Name', 'First Name', 'Year', 'Tm', 'Pos']
    for category in args:
        col_list.append(category)
    
    # slice nba dataframe
    df = data.loc[:,col_list]
    
    # because 'all' is a string, and not present anywhere in the df, if statements tell function
    # how to handle them    
    if team == 'all':
        df,
    else:
        df = df[df['Tm']==team]
    
    if position == 'all':
        df,
    else:
        df = df[df['Pos']==position]
        
        
    if len(df) < n:
        n = len(df)

    # default sorting is by the first stat category ([0]) and '.head(n)' handles the total 
    # number of records shown
    df = df.sort_values(args[0], ascending = ascending, na_position = 'last').head(n)
     
    # obvious ranking is important, so 'Rank' column can be added after sorting
    # then we reorder the columns so that 'Rank' is first and most obvious
    df['Rank'] = range(1, n+1)
    col_list.insert(0, 'Rank')
    df = df[col_list]

    
    # if you want outcome to be a useable df, default title = False will produce that, otherwise
    # we produce a prettier style object
    if title == True:
        print("Top " + str(n) + " player/seasons in " + str(args[0]))
        if len(df.Year.unique()) == 1:
            print("(" + str(int(max(df.Year))) + ")")
        else:
            print("(" + str(int(min(data.Year))) + " - " + str(int(max(data.Year))) + ")")
        print("(An asterisk indicates HOF)")
        return df.style.hide_index()
    else:
        return pd.DataFrame(df)


# ### Second Function: 'get_corrs'

# In[10]:


def get_corrs(feature, steps = 5, data = teams):
    """returns a df object of correlation coefficients where each year column marks the front
    end of an 'era' for which the end year is always the current year (2019 upon creation).
    data is default set to 'teams' from teams.csv--note that this means the default data includes
    two abbreviated seasons."""
    
    headers = list(range(min(data['Year']),max(data['Year']),steps))

    # we can use 5 year steps here just to give us more data points, but 5 is itself arbitrary. The game
    # has shifted (either by rule changes or in styles) approximately every 10 years, so 10 would work here
    #q as well
    
    eras = [] # correlation tables for basketball beginning at year marks from 1979 to 2014
              # every 5 years (i.e. 1979 - 2019, 1984 - 2019 and so on)
    for i in headers:
        df = data[data['Year'] >= i]
        corrs = df.corr().loc[feature,:]
        eras.append(corrs)
    
    corr_df = pd.DataFrame(eras, index = headers)
    corr_df = corr_df.transpose()

    return corr_df


# In[11]:


get_corrs('W', steps = 10)


# In[5]:




