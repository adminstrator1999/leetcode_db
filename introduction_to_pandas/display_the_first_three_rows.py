import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Use head function to retrieve first n number of rows
    :param employees:
    :return:
    """
    return employees.head(3)
