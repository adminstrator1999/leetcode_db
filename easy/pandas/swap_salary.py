import pandas as pd


# def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
#     def swap_gender(x):
#         if x == 'f':
#             return 'm'
#         return 'f'
#
#     salary['sex'] = salary['sex'].apply(swap_gender)
#     return salary
#
# def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
#     salary['sex'] = salary['sex'].apply(lambda x: 'f' if x == 'm' else 'm')
#     return salary

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary['sex'] = salary['sex'].replace({'m': 'f', 'f': 'm'})
    return salary


data = [[1, 'A', 'm', 2500], [2, 'B', 'f', 1500], [3, 'C', 'm', 5500], [4, 'D', 'f', 500]]
salary = pd.DataFrame(data, columns=['id', 'name', 'sex', 'salary']).astype(
    {'id': 'Int64', 'name': 'object', 'sex': 'object', 'salary': 'Int64'})

print(swap_salary(salary))
