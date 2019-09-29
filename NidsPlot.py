import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   
import seaborn as sns

#Open Dataset
df = pd.read_pickle('filesave.pkl')

#Create Dataframe for each manipulation
df1 = df
df2 = df
df3 = df
df4 = df
df5 = df
df6 = df
df7 = df
df8 = df


#DROPVALS
#print(df[df['x'].isnull()])


pd.options.mode.chained_assignment = None

#Drop Empty Age
df3['w4_a_refage'] = pd.to_numeric(df3['w4_a_refage'], errors='coerce')
df3 = df3.dropna(subset=['w4_a_refage'])
df3['w4_a_refage'] = df3['w4_a_refage'].astype(int)

df3.dropna(subset=['w4_a_refage'])

#Drop and plot Sleeps Per Week
df4['w4_a_slpw'] = pd.to_numeric(df4['w4_a_slpw'], errors='coerce')
df4 = df4.dropna(subset=['w4_a_slpw'])
df4['w4_a_slpw'] = df4['w4_a_slpw'].astype(int)

sns.distplot(df4['w4_a_slpw'])
plt.show()

#Drop Empty NetWorth
df5['w5_net_worth_i'] = pd.to_numeric(df['w5_net_worth_i'], errors='coerce')
df5 = df.dropna(subset=['w5_net_worth_i'])
df5['w5_net_worth_i'] = df5['w5_net_worth_i'].astype(int)

df5.dropna(subset=['w5_net_worth_i'])

#Drop and Plot Empty Debt
df6['w4_re_deb_i'] = pd.to_numeric(df6['w4_re_deb_i'], errors='coerce')
df6 = df6.dropna(subset=['w4_re_deb_i'])
df6['w4_re_deb_i'] = df6['w4_re_deb_i'].astype(int)

sns.distplot(df6['w4_re_deb_i'])
plt.show()


#Drop and plot Owner sales
"""
df7 = df
df7['w4_h_ownsellft'] = pd.to_numeric(df7['w4_h_ownsellft'], errors='coerce')
df7 = df7.dropna(subset=['w4_h_ownsellft'])
df7['w4_h_ownsellft'] = df7['w4_h_ownsellft'].astype(int)

sns.distplot(df7['w4_h_ownsellft'])
plt.show()
"""

#Count Housing Subsidies
#df['w4_h_sub'].value_counts()[:20]


#Plotting

df['w1_h_sub'].value_counts()[:20].plot(kind='barh')
plt.show()
#df['w2_h_sub'].value_counts()[:20].plot(kind='barh')
plt.show()
df['w3_h_sub'].value_counts()[:20].plot(kind='barh')
plt.show()
df['w4_h_sub'].value_counts()[:20].plot(kind='barh')
plt.show()
df['w5_h_sub'].value_counts()[:20].plot(kind='barh')
plt.show()

df['w1_h_lndgrn'].value_counts()[:20].plot(kind='barh')
plt.show()
df['w2_h_lndgrn'].value_counts()[:20].plot(kind='barh')
plt.show()
df['w3_h_lndgrn'].value_counts()[:20].plot(kind='barh')
plt.show()
df['w4_h_lndgrn'].value_counts()[:20].plot(kind='barh')
plt.show()
df['w5_h_lndgrn'].value_counts()[:20].plot(kind='barh')
plt.show()

