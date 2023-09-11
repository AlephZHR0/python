import os
import pandas as pd


def find_all_ubers_into_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Find all ubers into a dataframe
    """
    df = df[df['title'].str.contains('Uber')]
    return df[['date', 'amount']]


def merge_two_dfs(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Merge two dataframes
    """
    return pd.concat([df1, df2], axis=0)


start_date = input('Enter start date (YYYY-MM-DD): ')
all_dfs_merged = None
for file in os.listdir(os.getcwd()):
    if file.endswith(".csv"):
        if all_dfs_merged is None:
            all_dfs_merged = find_all_ubers_into_df(pd.read_csv(file))
        else:
            df = find_all_ubers_into_df(pd.read_csv(file))
            all_dfs_merged = merge_two_dfs(all_dfs_merged, df)

all_dfs_merged.sort_values(by=['date'], inplace=True)
all_dfs_merged.query('date >= @start_date', inplace=True)
total = all_dfs_merged['amount'].sum()
first_uber_date = all_dfs_merged['date'].iloc[0]
last_uber_date = all_dfs_merged['date'].iloc[-1]
print(f"Total de Uber no periodo de {first_uber_date} até {last_uber_date}: {total}")
