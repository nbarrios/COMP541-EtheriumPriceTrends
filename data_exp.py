from email import header
import pandas as pd
import scipy.stats as sp
from scipy.stats import chi2_contingency
from scipy.stats import chi2
import matplotlib.pyplot as plt

etherium_files = [
                    "Etherium Dataset/full_data__6__2017.csv",
                    "Etherium Dataset/full_data__6__2018.csv",
                    "Etherium Dataset/full_data__6__2019.csv",
                    "Etherium Dataset/full_data__6__2020.csv",
                    "Etherium Dataset/full_data__6__2021.csv",
                 ]
result = pd.concat([pd.read_csv(f) for f in etherium_files], ignore_index=True)
result.info()
print("\n")
pd.set_option('display.float_format', lambda x: '%.1f' % x)
print(result.describe())
print("\nMedian:")
print(result.median())
print("\nRange:")
print(result.max() - result.min())
print("\nMidrange:")
print((result.max() - result.min()) / 2)
print("\nMode:")
print(result.mode())
print("\nIQR:")
print(result.quantile(0.75) - result.quantile(0.25))
print("\nSkew:")
print(result.skew())
print("\nCovariance:")
print(result.cov())
print("\nCorrelation:")
print(result.corr())
print("\nPearson Correlation:")
print(result.corr(method='pearson'))

result.plot(x = 'timestamp', y = 'Open', kind = 'scatter')
plt.savefig("plots/time_vs_open.png")

"""
result.plot(x = 'timestamp', y = ['High','Low'], kind = 'scatter')
plt.savefig("plots/time_vs_highlow.png")
"""

result.plot(x = 'Volume', y = 'VWAP', kind = 'scatter')
plt.savefig("plots/volume_vs_vwap.png")

result.plot(x = 'Target', y = 'Open', kind = 'scatter')
plt.savefig("plots/target_vs_open.png")

"""
print("\nChi Square Test (Open, Close):")
table = pd.crosstab(result["High"], result["Low"])
chi2_test, p, dof, expected = sp.chi2_contingency(table)
prob = 0.95
critical = chi2.ppf(prob, dof)
round(critical, 3)
alpha = 1.0 - prob
print('dof=%d' % dof)
print('critical =%.3f, chi2_test_statistic=%.3f' % (critical, chi2_test))
if chi2_test >= critical:
   print("dependent rejects null hypothesis")
else:
   print("Independent (fails to reject null hypothesis")
print('Significance = %.3f, p = %.3f' % (alpha, p))
print("\n")
"""