import pandas as pd


def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.merge(products, on='product_id', how='left')
    df = df[df.order_date.between('2020-02-01', '2020-02-29')]
    df = df.groupby('product_name')['unit'].sum().reset_index()
    df = df[df['unit'] >= 100]
    return df


data = [[1, 'Leetcode Solutions', 'Book'], [2, 'Jewels of Stringology', 'Book'], [3, 'HP', 'Laptop'],
        [4, 'Lenovo', 'Laptop'], [5, 'Leetcode Kit', 'T-shirt']]
products = pd.DataFrame(data, columns=['product_id', 'product_name', 'product_category']).astype(
    {'product_id': 'Int64', 'product_name': 'object', 'product_category': 'object'})
data = [[1, '2020-02-05', 60], [1, '2020-02-10', 70], [2, '2020-01-18', 30], [2, '2020-02-11', 80],
        [3, '2020-02-17', 2], [3, '2020-02-24', 3], [4, '2020-03-01', 20], [4, '2020-03-04', 30], [4, '2020-03-04', 60],
        [5, '2020-02-25', 50], [5, '2020-02-27', 50], [5, '2020-03-01', 50]]
orders = pd.DataFrame(data, columns=['product_id', 'order_date', 'unit']).astype(
    {'product_id': 'Int64', 'order_date': 'datetime64[ns]', 'unit': 'Int64'})

print(list_products(products, orders))
