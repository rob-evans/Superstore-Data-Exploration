import pandas as pd
import matplotlib as plt
import seaborn as sns 
import chardet

with open(r'C:\Users\rob_e\Kaggle\Kaggle_Datasets\Supersore_Data-V_Chowdury\Data\Sample - Superstore.csv', 'rb') as rawdata:
    encoding_guess = chardet.detect(rawdata.read(10000))
print(encoding_guess)

superstore_data = pd.read_csv(r'C:\Users\rob_e\Kaggle\Kaggle_Datasets\Supersore_Data-V_Chowdury\Data\Sample - Superstore.csv', encoding = 'ISO-8859-1')

