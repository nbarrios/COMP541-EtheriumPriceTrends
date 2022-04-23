import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import zscore

scaler = MinMaxScaler()
d = {'Age Values':[13,15,16,16,19,20,20,21,22,22,25,25,25,25,30,33,33,35,35,35,35,36,40,45,46,52,70]}
df = pd.DataFrame(d)
print(df.describe())
#print(df.mode())
dd = pd.DataFrame(scaler.fit_transform(df), columns=['Age Values'])
#print(dd)
#print(zscore(df['Age Values']))

e = {'Observed': [[23,20], [16,20], [14,20], [19,20], [28,20]]}
de = pd.crosstab(index=e['Observed'])
print(de)
