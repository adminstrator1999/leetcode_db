import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', inplace=True)
    person.drop_duplicates(subset='email', inplace=True)


data = [[3, 'john@example.com'], [4, 'bob@example.com'], [1, 'john@example.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'int64', 'email':'object'})

delete_duplicate_emails(person)
print(person)


