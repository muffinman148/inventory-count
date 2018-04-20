#this program will take in data from a data.txt file , remove the outliers, then calculate the average
import numpy as np

#Takes in numbers from data.txt
with open ('data.txt') as f:
  for line in f:
    values = [int(num) for num in line.split()]
mean_duration = np.mean(values)
std_dev_one_test=np.std(values)

#drops outliers
def drop_outliers (x):
  if abs(x - mean_duration) <= std_dev_one_test:
    return x

#will be a list without outliers
values = filter(drop_outliers,values)
#print (values)
avg = sum(values)/float(len(values))
print(avg)
