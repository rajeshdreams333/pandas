import json
import pandas as pd

# with open('D:\OUTSIDE_STUFF\PANDAS\jsondata.json') as f:
#    data = json.load(f)

# print(data)

df=pd.read_json('D:\OUTSIDE_STUFF\PANDAS\jsondata.json')
print(df)
