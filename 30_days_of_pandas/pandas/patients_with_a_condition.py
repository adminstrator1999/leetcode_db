import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # patients = patients[any([w.startswith('DIAB1') for w in patients['conditions'].str.split(' ')])]
    condition = lambda conditions: any([w.startswith('DIAB1') for w in conditions.split(' ')])
    patients = patients[patients['conditions'].apply(condition)]
    return patients


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    patient = patients[patients['conditions'].str.contains(r'\bDIAB1')]
    return patient


data = [[1, 'Daniel', 'YFEV COUGH'], [2, 'Alice', ''], [3, 'Bob', 'DIAB100 MYOP'], [4, 'George', 'ACNE DIAB100'],
        [5, 'Alain', 'DIAB201']]
patients = pd.DataFrame(data, columns=['patient_id', 'patient_name', 'conditions']).astype(
    {'patient_id': 'int64', 'patient_name': 'object', 'conditions': 'object'})

print(find_patients(patients))
