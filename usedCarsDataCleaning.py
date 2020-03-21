import pandas as pd
import seaborn as sns
import re
used_cars=pd.read_csv("C:/Users/avakk/Downloads/vehicles.csv")  #Reading CSV

used_cars.shape
used_cars.info()
sns.heatmap(used_cars.isnull())
used_cars.isnull().sum() 
used_cars.drop(["region_url","image_url"],axis=1,inplace=True) #No contrbution towards prediction
used_cars.drop(["county","vin"],axis=1,inplace=True) #Null values


def isNaN(string):
    return string != string


def most_frequent(test_list): 
    counter = 0
    num = test_list[0] 
    
    for i in test_list: 
        curr_frequency = test_list.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
    return num 


for i in range(509577):
    if isNaN(used_cars["drive"][i]):
        regexp_drive=r"[0-9]WD"
        if isNaN(used_cars["description"][i]):
            pass
        else:
            drive=re.findall(regexp_drive,used_cars["description"][i])
            if len(drive)!=0:
                used_cars["drive"][i]=drive[0].lower()
    if isNaN(used_cars["transmission"][i]):
        regexp_trans=r"[A|a]utomatic|[M|m]anual"
        if isNaN(used_cars["description"][i]):
            pass
        else:
            trans=re.findall(regexp_trans,used_cars["description"][i])
            if len(trans)!=0:
                used_cars["transmission"][i]=trans[0].lower()
    if isNaN(used_cars["year"][i]):
        regexp_year=r"19[0-9][0-9]|20[0-9][0-9]"
        if isNaN(used_cars["description"][i]):
            pass
        else:
            years=re.findall(regexp_year,used_cars["description"][i])
            if len(years)!=0:
                used_cars["year"][i]=most_frequent(years)
    if isNaN(used_cars["fuel"][i]):
        regexp_fuel=r"[D|d]iesel|[G|g]as|[H|h]ybrid|[E|e]lectric"
        if isNaN(used_cars["description"][i]):
            pass
        else:
            fuel=re.findall(regexp_fuel,used_cars["description"][i])
            if len(fuel)!=0:
                used_cars["fuel"][i]=fuel[0].lower()


columns=["cylinders","transmission","fuel","year","drive","title_status","paint_color","type"]
for i in columns:
    used_cars[i]=used_cars[i].fillna(used_cars[i].value_counts().index[0])

used_cars["odometer"] = used_cars.groupby('year')['odometer'].apply(lambda x: x.fillna(x.mean()))
used_cars["odometer"] = used_cars["odometer"].fillna(method="ffill")

used_cars["manufacturer"]=used_cars["manufacturer"].fillna("unknown")
used_cars["model"]=used_cars["model"].fillna("unknown")
used_cars["model"].value_counts()
used_cars.drop(["description","size","lat","long"],axis=1,inplace=True)

