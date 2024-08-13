import pandas as pd


# def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
#     class_counts = courses['class'].value_counts()
#     valid_classes = class_counts[class_counts >= 5].index
#     return pd.DataFrame(valid_classes)

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # Group by class and count the number of students in each class
    class_counts = courses.groupby('class')['student'].count().reset_index()

    # Filter classes with 5 or more students
    result = class_counts[class_counts['student'] >= 5][['class']]

    return result


data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'],
        ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student': 'object', 'class': 'object'})

print(find_classes(courses))