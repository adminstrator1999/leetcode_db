import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    """
    Need to come back for this
    :param weather:
    :return:
    """
    return pd.pivot_table(weather, index='month', columns='city', values='temperature', aggfunc='max')