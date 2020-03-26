import pandas as pd
used_cars=pd.read_csv("C:/sem2/vehicles.csv") #Reading CSV
used_cars.shape
used_cars.info()

#sns.heatmap(used_cars.isnull())
used_cars.isnull().sum()
