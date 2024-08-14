import pandas as pd


def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    round2 = lambda x: round(x + 1e-9, 2)
    queries['quality'] = queries.rating/queries.position
    queries['poor_query_percentage'] = (queries['rating'] < 3) * 100
    return queries.groupby('query_name')[['quality', 'poor_query_percentage']].mean().apply(round2).reset_index()


data = [['Dog', 'Golden Retriever', 1, 5], ['Dog', 'German Shepherd', 2, 5], ['Dog', 'Mule', 200, 1],
        ['Cat', 'Shirazi', 5, 2], ['Cat', 'Siamese', 3, 3], ['Cat', 'Sphynx', 7, 4]]
queries = pd.DataFrame(data, columns=['query_name', 'result', 'position', 'rating']).astype(
    {'query_name': 'object', 'result': 'object', 'position': 'Int64', 'rating': 'Int64'})

print(queries_stats(queries))
