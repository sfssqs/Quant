import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df = get_price('000300.XSHG')
# df.query('index == ["2015-01-05", "2015-01-07"]')

df2 = pd.DataFrame(np.random.rand(10, 3), columns=list('abc'))
print df2

''' Query columns '''
print df2.query('(a < b) & (b < c)')

''' Data index '''
dates = pd.date_range('20160101', periods=6)

''' Initialize DataFrame '''
df3 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print df3

''' Add columns '''
df3['E'] = round(6, 5)
print df3

''' Delete columns '''
del df3['E']
print df3

''' Type change, dict '''
print df3.to_dict('dict')

''' Get columns as Series '''
print df3['A']
print df3.A

''' Get Head data '''
print df3.head()

''' Get Tail data '''
print df3.tail(3)

''' Show index; columns; data; '''
print df3.index
print df3.columns
print df3.values

''' Describe '''
print df3.describe()

''' Convert column and index '''
convert = df3.T
print convert.index

''' Sort by index '''
sort_index = df3.head(5).sort_index(axis=1, ascending=True)
print df3
print sort_index

''' Sort by value '''
sort_value = df3.head().sort(columns='B')
print df3
print sort_value

''' Description '''
print df3.shape

''' Select '''
print df3['A']
print df3.A

print df3[0:3]
print df3[0:1]

print '-------------------------------------'
print df3.loc['2016-01-01':'2016-01-05', 'A':'C']
print df3.loc['2016-01-01':'2016-01-05', ['A', 'C']]

''' Set value by label '''
dates = pd.date_range('20160101', periods=6)
df3.at[dates[0], 'A'] = 0
print df3

''' Set value by position '''
df3.iat[0, 2] = 11
print df3

''' Set value by numpy '''
df3.loc[:, 'D'] = np.array([5] * len(df3))
print df3

print '-------------------------------------'
print ''' IO Input/Output '''
df4 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print df4

print '\n'
df4.to_csv('foo.csv')
print pd.read_csv('foo.csv')

print '\n'
df4.to_hdf('foo.h5','df')
print pd.read_hdf('foo.h5','df')

print '\n'
df4.to_excel('foo.xlsx', sheet_name='Sheet1')
print pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
