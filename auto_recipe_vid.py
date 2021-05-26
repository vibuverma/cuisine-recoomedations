# For fetching recipe links

from pandas.io.parquet import FastParquetImpl
from youtubesearchpython import SearchVideos
import pandas as pd 

data= pd.read_csv("artifacts/cleaned_data.csv") 

# Creating empty column with name "recipe"
if "recipe" not in data.columns:
    data['recipe']= "empty"

try:
    for i in range(data.shape[0]):
        if data.loc[i, "recipe"] == "empty":
            dish= data.iloc[i,"name"] 

            search= SearchVideos(dish + " indian recipe in english", offset=1, mode="dict", max_results=1)
            print(i, dish)

            # storinh recipe video in appropriate index
            data.loc[i, "recipe"]= search.result()["search_result"][0]["link"].split("=")[1]

            #saving it to csv
            data.to_csv("cleaned_data.csv", index=False)
except: 
    print("API limit exeeded")