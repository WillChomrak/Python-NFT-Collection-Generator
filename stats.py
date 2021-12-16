import os
import json
import pandas as pd

# Put all attributes in this list - comma separated
all_attributes = ["Orange", "Yellow", "Green", "Blue", "Square", "Heart", "Triangle", "SQ1", "SQ2", "SQ3", "Live", "Laugh", "Love"]

dirname = os.path.dirname(__file__) 

NFT_metadata = dirname + "\Finished\\Allmetadata.json"

with open(NFT_metadata) as my_read_file:
    metaObj = json.load(my_read_file) # convert JSON back to python object
    keys = metaObj.keys() # key for each NFT

rows = []
# count number of times an attribute occurs in the Allmetadata file
for attribute in all_attributes:
    count = 0
    for key in keys:
        if attribute in metaObj[key]["attributes_all"]:
            count += 1
    rows.append([attribute, count])

df = pd.DataFrame(rows, columns=["Attribute", "Occurences"])

df.to_csv("stats.csv")
    