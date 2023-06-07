# # import pandas as pd
# # import numpy as np


# # # Creating empty series
# # ser = pd.Series()

# # print(ser)

# # # simple array
# # data = np.array(['g', 'e', 'e', 'k', 's'])

# # ser = pd.Series(data)
# # print(ser)

# import pandas as pd

# # Calling DataFrame constructor
# df = pd.DataFrame()
# print(df)

# # list of strings
# lst = ['Geeks', 'For', 'Geeks', 'is',
# 			'portal', 'for', 'Geeks']

# # Calling DataFrame constructor on list
# df = pd.DataFrame([lst,lst,lst])
# # print(df.iloc[0:2,3:5])
# print(df[0])
# # print(df)

# import pandas module
import pandas as pd

# create dataframe with 3 columns
data = pd.DataFrame({
	"id": [7058, 7059, 7072, 7054],
	"name": ['sravan', 'jyothika', 'harsha', 'ramya'],
	"subjects": ['java', 'python', 'html/php', 'php/js']})

print(data)
print(data.iat[1,1])
print(data['id'].loc[2])
# get the cell value using loc() function
# in name column and 1 row
print(data['id'].loc[data.index[0]])

# get the cell value using loc() function
# in name column and 2 row
print(data.index[1])
print('this is: ', data['name'].iloc[3])

# get the cell value using loc() function
# in subjects column and 4 row
print(data['subjects'].loc[data.index[3]])
