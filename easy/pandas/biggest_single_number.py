import pandas as pd


def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    counts = my_numbers['num'].value_counts()
    single_numbers = counts[counts == 1].index
    return single_numbers.max() if not single_numbers.empty else None


data = [[8], [8], [3], [3], [1], [4], [5], [6]]
my_numbers = pd.DataFrame(data, columns=['num']).astype({'num': 'Int64'})
print(biggest_single_number(my_numbers))
