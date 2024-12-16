# и создание самой таблицы

import pandas as pd

df = pd.DataFrame( columns = ["имя", "длина", "время", "точность", "дата" ])
df.to_csv('table.csv', index = False)

print(df)