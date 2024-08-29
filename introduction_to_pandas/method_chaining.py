import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    animals = animals[animals['weight'] > 100]
    animals.sort_values('weight', ascending=False, inplace=True)
    return animals['name']