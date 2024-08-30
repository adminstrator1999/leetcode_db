import numpy as np
import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = np.where(
    (employees['employee_id'] % 2 == 1) & (employees['name'].str[0] != 'M'),
    employees['salary'],
    0)
    employees.sort_values('employee_id', inplace=True)
    return employees[['employee_id', 'bonus']]

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0
    employees.sort_values('employee_id', inplace=True)
    employees.loc[(employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith('M')), 'bonus'] = employees['salary']
    return employees[['employee_id', 'bonus']]



data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype(
    {'employee_id': 'int64', 'name': 'object', 'salary': 'int64'})

print(calculate_special_bonus(employees))
