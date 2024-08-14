import pandas as pd


# def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
#     # 2019-06-28' and  '2019-07-27'
#     activity = activity[(activity['activity_date'] >= '2019-06-28') & (activity['activity_date'] <= '2019-07-27')]
#     activity = activity.drop_duplicates(['user_id', 'activity_date'])
#     activity = activity.groupby('activity_date')['user_id'].agg('count').reset_index()
#     return activity.rename(columns={'activity_date': 'day', 'user_id': 'active_users'})


def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    return activity[activity.activity_date.between("2019-06-28", "2019-07-27")].rename(
        columns={'activity_date': 'day', 'user_id': 'active_users'}).groupby('day')[
        'active_users'].nunique().reset_index()


data = [[1, 1, '2019-07-20', 'open_session'], [1, 1, '2019-07-20', 'scroll_down'], [1, 1, '2019-07-20', 'end_session'],
        [2, 4, '2019-07-20', 'open_session'], [2, 4, '2019-07-21', 'send_message'], [2, 4, '2019-07-21', 'end_session'],
        [3, 2, '2019-07-21', 'open_session'], [3, 2, '2019-07-21', 'send_message'], [3, 2, '2019-07-21', 'end_session'],
        [4, 3, '2019-06-25', 'open_session'], [4, 3, '2019-06-25', 'end_session']]
activity = pd.DataFrame(data, columns=['user_id', 'session_id', 'activity_date', 'activity_type']).astype(
    {'user_id': 'Int64', 'session_id': 'Int64', 'activity_date': 'datetime64[ns]', 'activity_type': 'object'})

print(user_activity(activity))
