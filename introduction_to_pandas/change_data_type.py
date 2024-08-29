import pandas as pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    """
    Use astype to change data types
    :param students:
    :return:
    """
    return students.astype({'grade': 'int64'})

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students
