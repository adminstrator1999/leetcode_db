import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    """
    Use drop_duplicates to drop multiple same rows
    :param customers:
    :return:
    """
    customers.drop_duplicates(subset=['email'], inplace=True)
    return customers