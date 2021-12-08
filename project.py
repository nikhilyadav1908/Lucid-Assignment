import pandas as pd
df = pd.read_csv(r'/users/nikhil/Downloads/in/in.csv')
print(df)
mean1 = df['volume'].means()
median1 = df['volume'].means()
std1 = df['volume'].std()
print("mean of the  volume: " + str(mean1))
print("median of the volume: " + str(median1))
print("standard deviation of the volume: " + str(std1))