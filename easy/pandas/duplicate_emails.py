import pandas as pd


# def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
#     email_counts = person.groupby('email').size()
#     duplicate_emails = email_counts[email_counts > 1].index
#     return pd.DataFrame(duplicate_emails, columns=['email'])

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return person.loc[person.duplicated('email') == True][['email']].drop_duplicates(keep='first')


data = [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype({'id': 'Int64', 'email': 'object'})

print(duplicate_emails(person))
