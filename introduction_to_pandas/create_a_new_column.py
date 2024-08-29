import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """
    To assign new column we can use assign function
    :param employees:
    :return:
    """
    return employees.assign(bonus = employees['salary'] * 2)

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees