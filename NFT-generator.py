import os
from PIL import Image
import random
import json
from config import config

dirname = os.path.dirname(__file__)

# Resize finshed NFTs
def resize_img(path, size):
    img = Image.open(path)
    dimensions = size, size
    img = img.resize(dimensions, resample=0)
    img.save(path)

def create_metadata(name, attributes):
    # Inserts the name and attributes list into the metadata schema and return the dict
    metadata_ = {
    "description": "My 10,000 NFT Collection - change this to describe your collection",
    "external_url": "https://YourNFT.COM ...",
    "image": "",
    "name": name,
    "attributes": [{
        "trait_type": "Base",
        "value": attributes[0]
      },
      {
        "trait_type": "Shape",
        "value": attributes[1]
      },
      {
        "trait_type": "Squiggle",
        "value": attributes[2]
      },
      {
        "trait_type": "Inspirational-message",
        "value": attributes[3]
      }
    ],
    "attributes_all": attributes
  }
    return metadata_

def generate_finished_images(num_imgs, layers):
    metadata = {}
    j = 1
    # These two lines randomize the order of NFTs output; This prevents lower probability attributes becoming more likely to occur later in the collection as no duplicates are permitted
    numberIndex = list(range(1, num_imgs + 1))
    random.shuffle(numberIndex)
    # pad_amount = len(str(num_imgs)) # This can be used to give the NFT numbers leading 0's ie. NFT # 0027

    while j <= num_imgs:

        # This selects one from each layer and appends all to a list
        selected_attrs = [] # ex. ['Mushroom', 'Gun', 'Girl Hair']
        selected_attrs_paths = []
        # duplicates_removed
        for layer in layers["layers"]:
            choice = random.choices(layer["filename"], layer["weights"])[0] # randomly selects an att based on weights
            selected_attrs.append(choice) # adds selected att to the list that makes up this NFT
            selected_attrs_paths.append(layer["path"] + choice)

        # Check if current attribute combination exists. "Continue" without creating or iterating if it does.
        duplicate = False
        # Compare this attribute combo against all existing attribute combos
        for key in metadata:
            if selected_attrs == metadata[key]["attributes_all"]:
                duplicate = True
                # don't need to test the rest of the NFTs if this att combo is a duplicate so "continue"
                continue

        # If this attribute combo is a duplicate, exit iteration without saving it and try another attribute combination
        if duplicate == True:
            # duplicates_removed += 1
            # print(duplicates_removed) uncomment this and above to see num of duplicates removed as as they occur
            continue

        # Open and combine images; save final product
        layered_img = Image.open(dirname + selected_attrs_paths[0] + ".png") # Opens the base layer image

        # Loop through all selected attribute paths
        for i, path in enumerate(selected_attrs_paths):
            if i > 0:
                next_layer = Image.open(dirname + path + ".png") # opens each image using its path
                layered_img.paste(next_layer, (0, 0), next_layer) # superimposes the image on top of the base

        name = str(numberIndex.pop(0)) # use this instead (right of this comment) if you want to prefix filename and include leading zeros name = "Prefix" + str(j).zfill(pad_amount)
        path = dirname + "\\finished\\img\\" + name + '.png'
        layered_img.save(path) # saves the image in the finished folder
        resize_img(path, 350)

        # Pass name and seleceted_attrs to create_metadata func. This returns dict
        # Add this dict to our metadata dict with NFT name as key
        metadata[name] = create_metadata(name, selected_attrs)

        j += 1
        # Write individual NFT metadata to JSON file
        with open(dirname + '\\Finished\\metadata\\' + name + '.json', 'w') as outfile:
            json.dump(metadata[name], outfile, indent=4)

    # Write all NFT metadata to JSON file
    with open(dirname + '\\Finished\\Allmetadata.json', 'w') as outfile:
        json.dump(metadata, outfile, indent=4)

# Change the number below to set number of NFTs required
generate_finished_images(40, config)