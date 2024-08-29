from unittest.mock import inplace

import pandas as pd

from easy.pandas.swap_salary import salary


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(salary = employees['salary'] * 2)



def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees