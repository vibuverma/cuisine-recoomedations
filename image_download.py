from bing_image_downloader import downloader
import pandas as pd
import os

data= pd.read_csv('cleaned_data.csv')
name= data['name']  #getting names of dishes from dataset

for n in name:
    path= "/image_dataset"+ n + " indian food"

    if os.path.exists(path):
        continue
    query_string= n + " indian food"
    downloader.download(query_string, limit=4, output_dir='static/image_dataset',
                        adult_filter_off=True, force_replace=False, timeout=60*5)