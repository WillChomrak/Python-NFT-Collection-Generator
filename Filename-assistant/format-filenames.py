import os
import pandas as pd
import json

dirname = os.path.dirname(__file__) 

csv_file = dirname + "\\layers.csv" # input 
txt_file = dirname + "\\asset-filenames.txt" # output

col_list = [
"Attributes_Layer_1", "Probs_Layer_1", "Attributes_Layer_2", "Probs_Layer_2", 
"Attributes_Layer_3", "Probs_Layer_3", "Attributes_Layer_4", "Probs_Layer_4", 
"Attributes_Layer_5", "Probs_Layer_5", "Attributes_Layer_6", "Probs_Layer_6"] # change to match your column headings

df = pd.read_csv(csv_file, usecols=col_list)

data_struct = {}

# adds a list of items (names or probs) for each column to metadata dict
for column in col_list:
    # removes blank cells, adds to list, sets that as value in dict with column name as key
    data_struct[column] = df[column].dropna().tolist()

# write to json file for easy copy/paste to NFT generator file
with open(txt_file, "w") as my_output_file:
    json.dump(data_struct, my_output_file, indent=4)
