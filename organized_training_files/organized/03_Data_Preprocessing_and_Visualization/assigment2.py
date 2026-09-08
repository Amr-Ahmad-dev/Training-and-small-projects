from py_compile import main

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_excel("C:\\Users\\01100\\Downloads\\CS50x Projects\\traning\\students_dataset.xlsx", engine='openpyxl')
print(data_frame.head(10))
print(data_frame.tail(10))
print(data_frame.info())
print(data_frame.shape)
print(data_frame.describe())
data_frame.dropna(inplace=True)
data_frame.drop_duplicates(inplace=True)
data_frame.drop_duplicates(subset=['Student_ID'], keep='first', inplace=True)
data_frame["Average"]=data_frame[['Math','Physics','Chemistry','English']].mean(axis=1)
data_frame["total"]=data_frame[['Math','Physics','Chemistry','English']].sum(axis=1)
data_frame["Grade "]=np.where(data_frame["Average"]>=90, 'A', np.where(data_frame["Average"]>=80, 'B', np.where(data_frame["Average"]>=70, 'C', np.where(data_frame["Average"]>=60, 'D', 'F'))))
sum_m=np.where( data_frame['Gender']=="M",1,0).sum()
sum_f=np.where( data_frame['Gender']=="F",1,0).sum()
print(sum_m)
print(sum_f)
h_average=data_frame['Average'].max()
l_average=data_frame['Average'].min()
print(h_average)
print(l_average)
print(data_frame[data_frame['Average'] >=85 ])
print(data_frame[data_frame['Attendance'] <=70 ])
data_frame.sort_values(by=['Average'], ascending=False, inplace=True)
print(data_frame.nlargest(10, 'Average'))
print(data_frame.nsmallest(10, 'Average'))
data_frame.loc["Average_row"]=data_frame.mean(axis=0,numeric_only=True)
drow,axsis=plt.subplots(2,2)
data_frame.loc["Average_row",["Math","Physics","Chemistry","English"]].plot(kind="bar",ax=axsis[0][0])
plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Mark")

print(data_frame)
print(data_frame.columns)
print(data_frame.index)
data_frame["Department"].value_counts().plot(
    ax=axsis[0][1],
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Department")

data_frame.loc[:,"Average"].plot(kind="hist",ax=axsis[1][0])

data_frame.loc[:,["Average","Name"]].head(10).plot(kind="line",ax=axsis[1][1])

plt.tight_layout()
plt.show()

data_frame.to_csv('C:\\Users\\01100\\Downloads\\CS50x Projects\\traning\\students_dataset_cleaned.csv')
print(data_frame.shape)
arr_marks=np.array(data_frame[['Math','Physics','Chemistry','English']])
print(arr_marks.shape)
print(arr_marks.ndim)
print(arr_marks.dtype)
first_row=arr_marks[0][0:]
first_coll=arr_marks[0:][0]
last_coll=arr_marks[0:][-1]
arr_marks=np.clip(arr_marks+5,None,100)

