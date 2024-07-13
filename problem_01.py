'''
Task 3
Description:
This task involves using the matplotlib
library to visualize data.

Responsibility:
Create a bar chart and a line chart using
Matplotlib to visualize data from a Pandas
DataFrame. Customize the charts with
labels, titles, and legends.

'''
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

#Reading data
df=pd.read_csv("D:\Python\Datasets\MyTips.csv")
# print("Displaying first 10rows of data : \n ")
# display(df.head(10))

# #Plotting scatter
# plt.scatter(df['day'],df['tip'])
# #Adding title
# plt.title("Scatter Plot")
# plt.xlabel('Day')
# plt.ylabel('Tip')
# plt.show()

# # Displaying Colorbar
# plt.scatter(df['day'],df['tip'],s=df['total_bill'],c=df['size'],cmap='viridis')
# #Adding title
# plt.title("Scatter Plot")
# plt.xlabel('Day')
# plt.ylabel('Tip')
# plt.show()
# #Adding color bars
# plt.colorbar(label='Size')
# plt.show()

 #Displaying Line graph

# plt.plot(df['tip'])
# plt.plot(df['size'])
# plt.title("Bar Chart")
# plt.xlabel('Day')
# plt.ylabel('Tip')
# plt.show()

#Displaying Bar Chart
# plt.bar(df['day'],df['tip'])
# #Adding title
# plt.title("Bar Chart")
# plt.xlabel('Day')
# plt.ylabel('Tip')
# plt.show()

#Displaying Histogram of tip 
# plt.hist(df['tip'],bins=10,edgecolor='black')
# plt.title("Histogram of Tips")
# plt.xlabel('Tip')
#plt.ylabel('Frequency')
#plt.show()