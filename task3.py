#Task 3: Data analysis using python(Reading a dataset csv file)
import pandas as pd
import matplotlib.pyplot as plt #ngoba sizo plot a graph

#Read the dataset
data = pd.read_csv(r"C:\Users\27789\Downloads\motor_insure.csv\motor_data11-14lats.csv")

#Inspect its column by displaying the first 10 rows
print(data.head(10))

#Display records for make and usage for seats_num that are more than 40
seats = data['SEATS_NUM'] >= 40
dfseats = data[seats]
print(dfseats[['MAKE','USAGE']])

#Plot a basic graph showing effective_yr on y-axes and carrying capacity on x-axes
plt.plot(data['CARRYING_CAPACITY'].head(25),data['EFFECTIVE_YR'].head(25))
plt.title("Carrying Capacity vs Effective Year")
plt.ylabel("Carrying_Capacity")
plt.xlabel("Effective_Year")
plt.show()