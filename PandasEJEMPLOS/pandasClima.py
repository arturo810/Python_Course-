import pandas as pd

df = pd.read_csv("C:\CursoPYTHON\PRACTICAS\python\csv\clima.csv")
head_df=df["Ciudad"]
print(head_df)
tail_df = df.tail()
print(tail_df)









