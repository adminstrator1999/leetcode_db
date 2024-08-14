import pandas as pd


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame,
                              examinations: pd.DataFrame) -> pd.DataFrame:
    examinations['taken'] = 1
    return students.merge(subjects, how='cross') \
        .merge(examinations, how='left', on=['student_id', 'subject_name']) \
        .groupby(['student_id', 'student_name', 'subject_name'], dropna=False)['taken'].sum() \
        .reset_index(name='attended_exams')


# def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame,
#                               examinations: pd.DataFrame) -> pd.DataFrame:
#     merge1 = students.merge(subjects, how='cross').sort_values(['student_id', 'subject_name'])
#     merge2 = examinations.groupby(['student_id', 'subject_name']).agg(attended_exams=('subject_name', 'count')).reset_index()
#     res = merge1.merge(merge2, on=['student_id', 'subject_name'], how='left').fillna(value={'attended_exams': 0})
#     # res = pd.merge(left=merge1, right=merge2, how='left', on=['student_id', 'subject_name']).fillna(value={'attended_exams': 0})
#     return res[['student_id', 'student_name', 'subject_name', 'attended_exams']]

data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]
students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype(
    {'student_id': 'Int64', 'student_name': 'object'})
data = [['Math'], ['Physics'], ['Programming']]
subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name': 'object'})
data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'], [13, 'Math'],
        [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype(
    {'student_id': 'Int64', 'subject_name': 'object'})

print(students_and_examinations(students, subjects, examinations))
