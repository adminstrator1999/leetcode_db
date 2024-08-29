import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    """
    Use dropna to get rid of missing data None
    :param students:
    :return:
    """
    students.dropna(subset=['name'], inplace=True)
    return students
