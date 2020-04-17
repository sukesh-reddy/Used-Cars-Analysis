from sklearn.model_selection import train_test_split
from sklearn import ensemble
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import column_or_1d

cleaned=pd.read_csv("C:/Users/avakk/Downloads/updatedcv.csv")
cleaned.drop(["url","lat","long","id","model","region"],axis=1,inplace=True)
cleaned["cylinders"]=cleaned["cylinders"].str.replace('cylinders','')

convert_dict={
        "cylinders":int
        }
cleaned=cleaned.astype(convert_dict)

cleaned.drop(cleaned[cleaned["title_status"]=="parts only"].index,inplace=True)
cleaned.drop(cleaned[cleaned["title_status"]=="missing"].index,inplace=True)
cleaned.drop(cleaned[cleaned["title_status"]=="lien"].index,inplace=True)

cleaned.drop(cleaned[cleaned["price"]<2000].index,inplace=True)
cleaned.drop(cleaned[cleaned["price"]>40000].index,inplace=True)

northeast=["ct","me","ma","nh","ri","vt","nj","ny","pa"]
midwest=["il","in","mi","oh","wi","ia","ks","mn","mo","ne","nd","sd"]
south=["de","fl","ga","md","nc","sc","va","wv","dc","ms","al","ky","tn","ar","tx","ok","la"]
west=["az","co","id","mt","nv","nm","ut","wy","wa","or","hi","ca","az","ak"]

for index, row in cleaned.iterrows():
    if(row["state"] in northeast):
        cleaned.at[index,"state"]="northeast"
    if(row["state"] in midwest):
        cleaned.at[index,"state"]="midwest"
    if(row["state"] in south):
        cleaned.at[index,"state"]="south"
    if(row["state"] in west):
        cleaned.at[index,"state"]="west"

yearmed=cleaned["year"].median()
cleaned["year"].fillna(yearmed)
for index, row in cleaned.iterrows():
    if(row["year"]>2020):
        cleaned.at[index,"year"]=yearmed

y=cleaned["price"]
x=cleaned.drop('price',axis=1)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

x_odomin=x_train["odometer"].min()
x_odomax=x_train["odometer"].max()

x_train["odometer"]=((x_train["odometer"]-x_odomin)/(x_odomax-x_odomin))

x_yearmin=x_train["year"].min()
x_yearmax=x_train["year"].max()

x_train["year"]=((x_train["year"]-x_yearmin)/(x_yearmax-x_yearmin)) 

y_trmin=y_train.min()
y_trmax=y_train.max()
y_train=((y_train-y_trmin)/(y_trmax-y_trmin)) 

x_test["odometer"]=((x_test["odometer"]-x_odomin)/(x_odomax-x_odomin))
x_test["year"]=((x_test["year"]-x_yearmin)/(x_yearmax-x_yearmin)) 

y_test=((y_test-y_trmin)/(y_trmax-y_trmin)) 

ordinal_columns=["cylinders"]

class LabelEncoder(LabelEncoder):
    def fit(self, y):
        y = column_or_1d(y, warn=True)
        self.classes_ = pd.Series(y).unique().sort()
        return self

ordinal_columns=["cylinders"]

for col in ordinal_columns:
     le = LabelEncoder()
     le.fit_transform(list(x_train[col].values))
     x_train[col] = le.transform(list(x_train[col].values))

for col in ordinal_columns:
    le.fit(list(x_test[col].values))
    x_test[col] = le.transform(list(x_test[col].values))
    
xx_train=pd.get_dummies(x_train)

xx_test=pd.get_dummies(x_test)
missing_cols=set(xx_train.columns)-set(xx_test.columns)
for val in missing_cols:
    xx_test[val]=0
xx_test=xx_test[xx_train.columns]