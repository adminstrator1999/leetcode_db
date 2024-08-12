import pandas as pd

data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype(
    {'id': 'Int64', 'name': 'object', 'salary': 'Int64', 'managerId': 'Int64'})


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # Merge the DataFrame with itself to get employees and their managers
    df = employee.merge(employee, left_on='managerId', right_on='id', how='inner')

    # Rename columns for clarity
    df = df.rename(columns={'name_x': 'Employee'})

    # Filter employees who earn more than their managers
    result = df.loc[df['salary_x'] > df['salary_y'], ['Employee']]

    return result


print(find_employees(employee))
