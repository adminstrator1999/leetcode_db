import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee.drop_duplicates(subset=['salary']).sort_values('salary', ascending=False)
    try:
        if N <= 0:
            raise IndexError
        return df.iloc[[N - 1], [1]].rename(columns={'salary': f'getNthHighestSalary({N})'})
    except IndexError:
        return pd.DataFrame([None], columns=[f'getNthHighestSalary({N})'])

data = [[1, 100], [2, 200], [3, 300], [4, 300]]
employee = pd.DataFrame(data, columns=['Id', 'Salary']).astype({'Id':'Int64', 'Salary':'Int64'})

print(nth_highest_salary(employee, 4))