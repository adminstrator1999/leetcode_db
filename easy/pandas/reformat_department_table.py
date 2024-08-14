import pandas as pd


def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df = department.pivot(index='id', columns='month', values='revenue')
    df = df.reindex(columns=months)
    df.rename(columns=lambda prefix: prefix + '_Revenue', inplace=True)
    df.reset_index(inplace=True)
    df.sort_values('id')
    return df




data = [[1, 8000, 'Jan'], [2, 9000, 'Jan'], [3, 10000, 'Feb'], [1, 7000, 'Feb'], [1, 6000, 'Mar']]
department = pd.DataFrame(data, columns=['id', 'revenue', 'month']).astype(
    {'id': 'Int64', 'revenue': 'Int64', 'month': 'object'})
print(reformat_table(department))
