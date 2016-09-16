from general import *
import pandas as pd

pd.set_option('display.width', None)
# pd.options.display.max_columns = None


# f = open('checks_short.txt', 'r')
# my_list = []
# for line in f:
#     lin = line.strip().split(',')
#     my_list.append(lin[23])
# f.close()
#
# print (my_list)
#
# zbir = 0
# for item in my_list:
#     zbir += float(item)
# print (zbir)
#
# append_to_file('sabrano.txt', str(zbir))

# with open('185_ture.txt', 'r') as f:
#     for line in f:
#         print (line)


lista = [4, 14, 15, 16, 17, 18, 19, 20, 21, 23]
df = pd.read_csv('185_ture.txt', usecols=lista,
                 names=['Period', 'Truck#', 'Ship Date', 'Delivery Date', 'Trip#', 'Driver', 'Booking', 'Origin',
                        'Destination', 'Grand Total'])

df['Ship Date'] = df['Ship Date'].str.extract('(../../....)')
df['Delivery Date'] = df['Delivery Date'].str.extract('(../../....)')

# df.to_csv('sredjen.csv') # df.to_csv(file_name, sep='\t', encoding='utf-8')

# print(df)

# mask = (df['Driver'] == 'MAR-STO') # Vozaci: NEGO-VELJ, NEMA-POPO, STEV-YEAH, MAR-STO
#
# df1 = df.loc[mask]
#
# print (df1)

df2 = df[['Origin', 'Destination']]
# assert isinstance(df2.head, object)
print(df2)
