import pandas as pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Use pd.concat to concatenate multiple Dataframes or Series
    :param df1:
    :param df2:
    :return:
    """
    return pd.concat([df1, df2])