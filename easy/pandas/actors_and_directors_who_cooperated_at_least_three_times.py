import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(by=['actor_id', 'director_id']).size().reset_index(name='count')
    return df[df['count'] >=3][['actor_id', 'director_id']]


data = [[1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 4], [2, 1, 5], [2, 1, 6]]
actor_director = pd.DataFrame(data, columns=['actor_id', 'director_id', 'timestamp']).astype(
    {'actor_id': 'int64', 'director_id': 'int64', 'timestamp': 'int64'})

print(actors_and_directors(actor_director))