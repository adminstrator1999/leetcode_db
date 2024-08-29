import pandas as pd


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    """
    Use rename function to rename columns
    :param students:
    :return:
    """
    renames = {"id": "student_id",
               "first": "first_name",
               "last": "last_name",
               "age": "age_in_years"}
    return students.rename(columns=renames)