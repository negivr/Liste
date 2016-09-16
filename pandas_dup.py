import os
import pandas as pd


# pd.set_option('display.max_columns', 5000)
# pd.set_option('display.max_columns', None)
# pd.options.display.max_columns = 500
# pd.options.display.max_colwidth = 500

# pd.set_option('display.width', 1000)
# pd.options.display.max_rows = 999

print(pd.get_option('display.max_columns'))
pd.set_option('display.max_columns', 60)
print(pd.get_option('display.max_columns'))



# cols = ['Route', 'Pickup Date/Time', 'Delivery Date/Time', 'Truck', 'Driver 1']
#
#
# df = pd.read_csv('C:/Users/office/OneDrive/Circle32/sve ture.csv', usecols=cols)
#
# # print(df.head())
#
#
# print(df[df['Driver 1'] == 'TOMISLAV  OTASEVIC'])










