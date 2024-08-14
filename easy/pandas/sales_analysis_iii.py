import pandas as pd
from datetime import datetime


# def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
#     start_date = datetime.strptime('2019-01-01', '%Y-%m-%d')
#     end_date = datetime.strptime('2019-03-31', '%Y-%m-%d')
#     sales = sales.merge(product, on='product_id')

#     df = sales[(sales['sale_date'] < start_date) | (sales['sale_date'] > end_date)]
#     res = sales[~sales['product_id'].isin(df['product_id'])]
#     return res[['product_id', 'product_name']]

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    # Group the 'sales' DataFrame by 'product_id' and calculate the minimum and maximum sale dates for each product
    sales = sales.groupby('product_id')['sale_date'].agg(['min', 'max']).reset_index()

    # Filter the sales data to include only records with sale dates between January 1, 2019, and March 31, 2019
    sales = sales[(sales['min'] >= '2019-01-01') & (sales['max'] <= '2019-03-31')]

    # Merge the filtered sales data with the 'product' DataFrame based on 'product_id', keeping only 'product_id' and
    # 'product_name' columns
    result = pd.merge(sales, product, on='product_id', how='inner')[['product_id', 'product_name']]

    # Return the resulting DataFrame
    return result


data = [[1, 'S8', 1000], [2, 'G4', 800], [3, 'iPhone', 1400]]
product = pd.DataFrame(data, columns=['product_id', 'product_name', 'unit_price']).astype(
    {'product_id': 'Int64', 'product_name': 'object', 'unit_price': 'Int64'})
data = [[1, 1, 1, '2019-01-21', 2, 2000], [1, 2, 2, '2019-02-17', 1, 800], [2, 2, 3, '2019-06-02', 1, 800],
        [3, 3, 4, '2019-05-13', 2, 2800]]
sales = pd.DataFrame(data, columns=['seller_id', 'product_id', 'buyer_id', 'sale_date', 'quantity', 'price']).astype(
    {'seller_id': 'Int64', 'product_id': 'Int64', 'buyer_id': 'Int64', 'sale_date': 'datetime64[ns]',
     'quantity': 'Int64', 'price': 'Int64'})

print(sales_analysis(product, sales))