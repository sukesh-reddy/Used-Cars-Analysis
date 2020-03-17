import pandas as pd
used_cars=pd.read_csv("C:/Users/avakk/Downloads/vehicles.csv")

used_cars.shape
used_cars.info()
used_cars.isnull().sum()
used_cars.drop(["county"],axis=1,inplace=True)
