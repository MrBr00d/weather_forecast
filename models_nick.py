import numpy as np
import pandas as pd

def get_months(data: pd.DataFrame) -> pd.DataFrame:
    df = data.copy()
    month_name = []
    for row in range(len(df)):
        month_name.append(df["date"][row].month_name())
    df["month"] = month_name
    a = pd.get_dummies(df["month"])
    df = df.join(a)
    df.drop("month", axis=1, inplace=True)
    return df

def make_sin(len_sin: int, period: int, offset: int=0, amplitude: int=1, mean: int=0):
    t = np.linspace(0,len_sin,len_sin)
    sinwave = amplitude * np.sin(2*np.pi * t/period-offset)+mean
    return sinwave

def create_lag(data, lag_cols, lag_num):
    """
    Creates a lag variable that lags begind the other variables.
    - data: a pandas dataframe
    - lag_cols: either a str or a list of strings containing the columns you want to create lags for
    - lag_num: either a int or list of int containing the numer of rows you want to create a lag for
    This function only works with 1 group.
    """
    for col in lag_cols:
        for num in lag_num:
            data[f'{col}_lag{num}'] = data[col].shift(num)
    
    data = data.iloc[max(lag_num):,]
    return data