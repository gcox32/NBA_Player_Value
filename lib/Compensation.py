#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
pd.set_option('mode.chained_assignment', None)


# In[2]:


drop = 'Unnamed: 0'

seasons = pd.read_csv('../data/labeled_seasons.csv').drop(drop, axis = 1)

caps = pd.read_csv('../data/salary_cap_history.csv').drop(drop, axis = 1)
caps = caps.rename(columns = {'year':'Year'})

teams = pd.read_csv('../data/teams.csv', sep = '\t').drop(drop, axis = 1)
teams = teams[['Tm','Year','W','L','W/L%','Rank']]


# In[3]:


seasons_with_caps = pd.merge(seasons, caps, on = 'Year', how = 'left')
full = pd.merge(seasons_with_caps, teams, on = ['Tm','Year'])
full.columns


# In[23]:


def assessment(year = 'any', cluster = 'any', stat = 'WS', highseed = False):
    """Takes year, cluster, and stat as inputs and outputs a boolean for whether a player is overpaid. 
    Signifying highseed as True sets the bar higher for establishing value."""
    if year == 'any':
        df = full
    else:    
        df = full[full.Year == year].loc[:,['Full Name','Tm','Year','cluster',
                                            'salary','salary_cap','G','GS',
                                            'MP','PER','VORP','WS','USG%','W',
                                            'L','BPM']]
    df['burden'] = round(df['salary']/df['salary_cap'],3)
    
    if year != 'any':
        df = df[['Full Name','Tm','W','L','salary','salary_cap','burden','cluster', stat]]
    else:
        df = df[['Full Name','Year','Tm','W','L','salary','salary_cap','burden','cluster', stat]]
        df.Year = df.Year.astype('int')
        
    if cluster != 'any':
        cluster_avg = df[df.cluster == cluster].groupby('cluster').mean().salary[0]
        df['cluster_avg'] = cluster_avg
        df = df[df.cluster == cluster]
        df = df.drop(columns = ['cluster','cluster_avg'], axis = 1)
    
    df.salary = df.salary.astype('int')
    
    
    if highseed == False:
        wincount = 44
    else:
        wincount = 49
    
    if stat == 'WS':
        df['exp_WS'] = round(df.burden * wincount,1)
        df['overpaid'] = df.exp_WS > df.WS
    elif stat == 'BPM': ########################### this calculation needs work #############################
        df['exp_BPM'] = round(df.burden * ((wincount * 29.03) - 1190.63),1)
        df['overpaid'] = df.exp_BPM > df.BPM
    
    
    compensation = df.sort_values('burden', ascending = False)
    
    if year != 'any':
        print('Salary cap for '+str(year)+':\t',str(compensation.iloc[0,5]))
        compensation = compensation.drop(columns = 'salary_cap')
        
    if cluster != 'any':
        print(cluster + ' average salary: ' + str(int(cluster_avg)))
    
    return compensation


# In[1]:


#df = assessment(year = 2018, cluster = 'Versatile Forward')

#df.sort_values('WS', ascending = False)

