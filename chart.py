#importing libraries 
import pandas as pd
import matplotlib.pyplot as plt
#%pylab inline

#open file using the read function 
data = pd.read_csv("trainset.csv")
data.head()

#defining x and y axis 
x = []
y = []

#plotting data for columns 1 and 3
for column in data:
        x(column[1])
        y(int(column[3]))

#defining x and y axis label, and title 
plt.bar(x, y)
plt.xlabel('Date')
plt.ylabel('High')
plt.title('Trainset')
plt.legend()
plt.show()




