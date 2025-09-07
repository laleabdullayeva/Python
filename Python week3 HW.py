#sual1
import pandas as pd
df=pd.read_csv("C:/Users/Admin/Downloads/fifa19.csv")
#sual2
print(df.head(12))
#sual3
df.info()
#sual4
result=df.shape[0]
print(result)
#sual5
print(df.columns)
#sual6
print(df.iloc[4999])
#sual7
print(df["user_id"])
#sual8
result=df.sort_values(by=["Club","Name"])
print(result)
#sual9
df.filtered=df[df["Overall"]>90]
print(df.filtered)
#sual10
result=df.drop("Unnamed: 0",axis=1)
print(result)
#sual11
print(df["Position"].nunique())
#sual12
print(df.isnull().sum())
#sual13
df["Release Clause"]=df["Release Clause"].fillna("unknown")
print(df["Release Clause"].isnull().sum())
#sual14
result=df["Age"].mean()
print(result)
#sual15
max_shot=df["ShotPower"].max()
print(max_shot)
#sual16
max_shot=df["ShotPower"].max()
player_max_shot=df[df["ShotPower"]==max_shot]
print(player_max_shot)
#sual17
result=df.describe()
print(result)