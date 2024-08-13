import pandas as pd


# def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
#     return triangle.assign(
#         triangle=triangle.apply(
#             lambda r: 'Yes'
#             if (r.x + r.y > r.z and r.x + r.z > r.y and r.y + r.z > r.x)
#             else 'No',
#             axis=1
#         )
#     )


def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle["triangle"] = ((triangle["x"] + triangle["y"] > triangle["z"]) &
                            (triangle["z"] + triangle["y"] > triangle["x"]) &
                            (triangle["x"] + triangle["z"] > triangle["y"]))
    triangle["triangle"] = triangle["triangle"].apply(lambda x: "Yes" if x else "No")
    return triangle


data = [[13, 15, 30], [10, 20, 15]]
triangle = pd.DataFrame(data, columns=['x', 'y', 'z']).astype({'x': 'Int64', 'y': 'Int64', 'z': 'Int64'})
print(triangle_judgement(triangle))
