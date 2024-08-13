import pandas as pd
from pandas.core.groupby import DataFrameGroupBy, SeriesGroupBy


def largest_orders(orders: pd.DataFrame) -> DataFrameGroupBy | SeriesGroupBy:
    return orders['customer_number'].mode().to_frame()


data = [[1, 1], [2, 2], [3, 3], [4, 3]]
orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype(
    {'order_number': 'Int64', 'customer_number': 'Int64'})

print(largest_orders(orders))
