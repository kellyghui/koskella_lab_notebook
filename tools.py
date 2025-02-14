import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

def clean_and_transpose(df, start_row=32, end_row=106):
    df = df.iloc[start_row:end_row].T
    df.columns = df.iloc[0]
    df.index = pd.to_numeric(df.iloc[:, 0], errors='coerce') / 3600
    df = df.iloc[1:, 2:].apply(pd.to_numeric, errors='coerce')
    df.columns.name = 'Series'
    return df

def phage_conc_sep(df):
    no_phage = df.filter(regex=r'^[A-H][1-6]$')
    tenthousand_phage = df.filter(regex=r'^[A-H](?:[7-9]|1[0-2])$')
    return no_phage, tenthousand_phage

def plot_timeseries(dataframe, title = None, legend_title = 'Series'):
    plt.figure(figsize=(11, 6))
    for column in dataframe.columns:
        sns.scatterplot(data=dataframe, x=dataframe.index, y=dataframe[column], label=column, s=11)
    plt.xlabel('Time (hr)')
    plt.ylabel('OD reading') 
    plt.title(title)
    plt.legend(title=legend_title, bbox_to_anchor=(1.05, 1.0), loc='upper left', ncol=3)
    plt.tight_layout() 
    plt.show()
    
def remove_outliers(df, fifteen_min = 1, lower_bound = 0.15, upper_bound = 0.25):
    df = df.loc[:, (df.iloc[fifteen_min] > lower_bound) & (df.iloc[fifteen_min] < upper_bound)]
    return df

#returns whether curve is normal or not
#p < 0.05 is normal, p > 0.05 is not normal
def AUC_graph(df, title = None):
    auc_values = {col: np.trapz(df[col], x=df.index) for col in df.columns}
    sns.histplot(auc_values.values(), bins=15, kde=True)
    plt.xlabel('AUC Values', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.title(title, fontsize=16)
    return stats.normaltest(list(auc_values.values()))

def rsquared(x, y):
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)
    return r_value**2

def plot_with_r_squared(df, x_col, y_col, lower = 0, upper=20, decimals=4, title = None):
    df_filtered = df[(df[x_col] < upper) & (df[x_col] > lower)]
    r_squared = rsquared(df_filtered[x_col], df_filtered[y_col])
    sns.lmplot(data=df_filtered, x=x_col, y=y_col, fit_reg=True, height=4, aspect=1.8)
    plt.text(0.88, 0.95, f"$R^2 = {r_squared:.{decimals}f}$", transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', horizontalalignment='right')
    plt.xlabel(f"OD at {x_col}")
    plt.ylabel(f"OD at {y_col}")
    plt.title(title)
    plt.show()
