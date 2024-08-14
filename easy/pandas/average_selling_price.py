import pandas as pd


# def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
#     df = prices.merge(units_sold, on='product_id', how='left')
#     df = df[df['purchase_date'].between(df.start_date, df.end_date)]
#
#     def weighted_mean(df, value, weight):
#         v, w = df[value], df[weight]
#         return (v*w).sum() / w.sum()
#     df = df.groupby('product_id').apply(weighted_mean, 'price', 'units')
#     main = df.round(2).rename('average_price').reset_index()
#
#     # for some products we have a price but no sales, for whatever reason LC demands we return zero avg price
#     priceIds = set(prices['product_id'].unique())
#     soldIds = set(units_sold['product_id'].unique())
#     missingIds = priceIds.difference(soldIds)
#     fill = pd.DataFrame({'product_id': list(missingIds), 'average_price': [0]*len(missingIds)})
#     return pd.concat([main, fill])

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:

    merged = units_sold.merge(prices, on='product_id', how='right')
    merged = merged[merged.purchase_date.isna() | merged.purchase_date.between(merged.start_date, merged.end_date)]
    merged['value'] = merged.units * merged.price

    grouped = merged.groupby('product_id')

    return (
            grouped.value.sum() / grouped.units.sum().replace({0: pd.NA})
    ).fillna(0).round(2).rename('average_price').to_frame().reset_index()


data = [[1, '2019-02-17', '2019-02-28', 5], [1, '2019-03-01', '2019-03-22', 20], [2, '2019-02-01', '2019-02-20', 15],
        [2, '2019-02-21', '2019-03-31', 30]]
prices = pd.DataFrame(data, columns=['product_id', 'start_date', 'end_date', 'price']).astype(
    {'product_id': 'Int64', 'start_date': 'datetime64[ns]', 'end_date': 'datetime64[ns]', 'price': 'Int64'})
data = [[1, '2019-02-25', 100], [1, '2019-03-01', 15], [2, '2019-02-10', 200], [2, '2019-03-22', 30]]
units_sold = pd.DataFrame(data, columns=['product_id', 'purchase_date', 'units']).astype(
    {'product_id': 'Int64', 'purchase_date': 'datetime64[ns]', 'units': 'Int64'})

print(average_selling_price(prices, units_sold))
