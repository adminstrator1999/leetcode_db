import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.drop_duplicates('salary').sort_values('salary', ascending=False)
    try:
        return df.iloc[[1], [1]].rename(columns={'salary': 'SecondHighestSalary'})
    except IndexError:
        return pd.DataFrame([None], columns=['SecondHighestSalary'])


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee['salary'].drop_duplicates()
    employee = employee.sort_values(ascending=False)
    if len(employee) < 2:
        return pd.DataFrame({'SecondHighestSalary' : [None]})
    else:
        return pd.DataFrame({'SecondHighestSalary' : [employee.iloc[1]]})

data = [[1, 100]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
print(second_highest_salary(employee))
