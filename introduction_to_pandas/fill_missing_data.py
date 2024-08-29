import pandas as pd


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    """
    Use fillna to fill missing data with value
    :param products:
    :return:
    """
    products.fillna(value={'quantity': 0}, inplace=True)
    return products
