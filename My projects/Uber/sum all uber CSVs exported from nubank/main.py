import os
import pandas as pd
from datetime import datetime


def find_all_ubers_and_99_into_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Find all ubers into a dataframe
    """
    df = df.query("title.str.contains('Uber') or title.str.contains('99')")
    return df[['date', 'amount']]


def merge_two_dfs(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Merge two dataframes
    """
    return pd.concat([df1, df2], axis=0)


def convert_date_to_yyyy_mm_dd(date: str) -> str:
    """
    Convert date to yy/mm/dd
    """
    date = date.split('/')
    return f"{date[2]}-{date[1]}-{date[0]}"
    

start_date = input('Enter start date (DD/MM/YYYY): ')
start_date = convert_date_to_yyyy_mm_dd(start_date)

end_date = input('Enter end date (DD/MM/YYYY) or press ".": ')
if end_date == ".":
    end_date = datetime.now().strftime("%Y-%m-%d")
else:
    end_date = convert_date_to_yyyy_mm_dd(end_date)

all_dfs_merged = None
for file in os.listdir(os.getcwd()):
    if file.endswith(".csv"):
        if all_dfs_merged is None:
            all_dfs_merged = find_all_ubers_and_99_into_df(pd.read_csv(file))
        else:
            df = find_all_ubers_and_99_into_df(pd.read_csv(file))
            all_dfs_merged = merge_two_dfs(all_dfs_merged, df)

all_dfs_merged.sort_values(by=['date'], inplace=True)
all_dfs_merged.query('date >= @start_date and date <= @end_date', inplace=True)

total = all_dfs_merged['amount'].sum()
if total > 0:
    first_uber_date = all_dfs_merged['date'].iloc[0]
    last_uber_date = all_dfs_merged['date'].iloc[-1]
    print(f"Total de Uber/99 no periodo de {first_uber_date} até {last_uber_date}: {total:.2f}")
else:
    print(f"Não houve Uber/99 no periodo de {start_date} até {end_date}")