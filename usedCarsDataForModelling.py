import pandas as pd
import numpy
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_squared_error
from math import sqrt

cleaned=pd.read_csv("C:/Users/avakk/Downloads/updatedcv.csv")
cleaned.drop(["url","lat","long","id","model","region"],axis=1,inplace=True)

cleaned.drop(cleaned[cleaned["title_status"]=="parts only"].index,inplace=True)
cleaned.drop(cleaned[cleaned["title_status"]=="missing"].index,inplace=True)
cleaned.drop(cleaned[cleaned["title_status"]=="lien"].index,inplace=True)
y=cleaned["price"]
x=cleaned.drop('price',axis=1)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
x_train[x_train["year"]>2020]=x_train["year"].median()
x_train["year"].fillna(x_train["year"].median())

x_odomin=x_train["odometer"].min()
x_odomax=x_train["odometer"].max()

x_train["odometer"]=((x_train["odometer"]-x_odomin)/(x_odomax-x_odomin))
x_yearmin=x_train["year"].min()
x_yearmax=x_train["year"].max()
x_train["year"]=((x_train["year"]-x_yearmin)/(x_yearmax-x_yearmin)) 

ytrmed=y_train.median()
y_train[y_train<2000]=ytrmed
y_train[y_train>40000]=ytrmed
y_trmin=y_train.min()
y_trmax=y_train.max()
y_train=((y_train-y_trmin)/(y_trmax-y_trmin)) 

northeast=["ct","me","ma","nh","ri","vt","nj","ny","pa"]
midwest=["il","in","mi","oh","wi","ia","ks","mn","mo","ne","nd","sd"]
south=["de","fl","ga","md","nc","sc","va","wv","dc","ms","al","ky","tn","ar","tx","ok","la"]
west=["az","co","id","mt","nv","nm","ut","wy","wa","or","hi","ca","az","ak"]

for index, row in x_train.iterrows():
    if(row["state"] in northeast):
        x_train.at[index,"state"]="northeast"
    if(row["state"] in midwest):
        x_train.at[index,"state"]="midwest"
    if(row["state"] in south):
        x_train.at[index,"state"]="south"
    if(row["state"] in west):
        x_train.at[index,"state"]="west"
        
xx_train=pd.get_dummies(x_train)

x_test[x_test["year"]>2020]=x_train["year"].median()
x_test["year"].fillna(x_train["year"].median())

x_test["odometer"]=((x_test["odometer"]-x_odomin)/(x_odomax-x_odomin))
x_test["year"]=((x_test["year"]-x_yearmin)/(x_yearmax-x_yearmin)) 

y_test[y_test<2000]=ytrmed
y_test[y_test>40000]=ytrmed

y_test=((y_test-y_trmin)/(y_trmax-y_trmin)) 

for index, row in x_test.iterrows():
    if(row["state"] in northeast):
        x_test.at[index,"state"]="northeast"
    if(row["state"] in midwest):
        x_test.at[index,"state"]="midwest"
    if(row["state"] in south):
        x_test.at[index,"state"]="south"
    if(row["state"] in west):
        x_test.at[index,"state"]="west"
        
xx_test=pd.get_dummies(x_test)

missing_cols=set(xx_train.columns)-set(xx_test.columns)
for val in missing_cols:
    xx_test[val]=0
xx_test=xx_test[xx_train.columns]