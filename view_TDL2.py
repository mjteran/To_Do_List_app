import pandas as pd

task_l = [['cantar', 'high', '2024-10-15'], ['comer', 'medium', '2024-10-15'], ['jump', 'low', '2024-10-16'],
          ['go', 'medium', '2024-10-14']]

df = pd.DataFrame(task_l, columns=['Task', 'Priority', 'Date'])     # panda dataFrame
df['Date'] = pd.to_datetime(df['Date'])                             # 'Date' to datetime for sorting
# first sort by Date
df.sort_values(by=['Date'], ascending=True, inplace=True)           # sort 'Date' in ascending order
# second sort by Priority
df['Priority_V'] = df['Priority'].map({'high':1, 'medium':2, 'low':3})  # create a column with priorities
df_sorted = df.sort_values(by=['Priority_V'])                       # sort by Priority values
print(df_sorted)
