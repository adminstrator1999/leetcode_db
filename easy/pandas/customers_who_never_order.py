import pandas as pd


# def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
#     df = customers.merge(orders, left_on='id', right_on='customerId', how='left')
#     df.rename(columns={'name': 'Customers'}, inplace=True)
#     df = df[df['id_y'].isnull()]
#     return df.loc[:, ['Customers']]

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    names = customers[~customers['id'].isin(orders['customerId'])]['name']
    return pd.DataFrame({'Customers': names})


data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
data = [[1, 3], [2, 1]]
orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id': 'Int64', 'customerId': 'Int64'})
print(find_customers(customers, orders))
