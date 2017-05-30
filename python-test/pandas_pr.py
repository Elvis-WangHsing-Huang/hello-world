# practice pandas and matplotlib.pyplot

import pandas as pd
import matplotlib.pyplot as plt

#read a csv file into a dataframe
df = pd.read_csv("city.csv", index_col =0)

print "all data:"
print df

print "\n\nall cities with pop > 1000K"
large_city = df['Population']>1000000
# show four columns of the large cities with population > 1M
print df[large_city].loc[:, ['City', "Population", "Man", "Average_age"]]

# iterate through the list to show the male/female percentage of each city
