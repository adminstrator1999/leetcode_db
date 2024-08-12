import pandas as pd


# def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
#     df = employee.merge(bonus, on='empId', how='left')
#     df = df[(df['bonus'] < 1000) | (df['bonus'].isna())]
#     return df[['name', 'bonus']]


def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(bonus, on='empId', how='left')[['name', 'bonus']]
    return df[(df['bonus'] < 1000) | (df['bonus'].isna())]


data = [[3, 'Brad', None, 4000], [1, 'John', 3, 1000], [2, 'Dan', 3, 2000], [4, 'Thomas', 3, 4000]]
employee = pd.DataFrame(data, columns=['empId', 'name', 'supervisor', 'salary']).astype(
    {'empId': 'Int64', 'name': 'object', 'supervisor': 'Int64', 'salary': 'Int64'})
data = [[2, 500], [4, 2000]]
bonus = pd.DataFrame(data, columns=['empId', 'bonus']).astype({'empId': 'Int64', 'bonus': 'Int64'})
print(employee_bonus(employee, bonus))