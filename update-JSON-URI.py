import os
from os.path import isfile, join
import json

dirname = os.path.dirname(__file__) 
metadata_path = dirname + "\\Finished\\metadata"

IPFS_URI = "ipfs://<yourCID>/" # This will need to be changed to a list of every new URI in a way 
                                # that it can be matched with the appropriate NFT metadata file

def updateURI(folder):
    # Creates a list of the files in the specified directory (after checking if each item is a file or not)
    onlyFiles = [f for f in os.listdir(folder) if isfile(join(folder, f))]
    # Cycle through each file and make the change.
    for file in onlyFiles:
        with open(join(folder, file), "r+") as outfile:
            data = json.load(outfile) # convert JSON back to python object
            full_URI = IPFS_URI + data["name"] + ".png"
            data["image"] = full_URI # write over image value
            outfile.seek(0) # reset file position to the beginning.
            json.dump(data, outfile, indent=4) # rewrite the whole file with the altered content

updateURI(metadata_path)