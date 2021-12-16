# Python-NFT-Collection-Generator
<h2>A NFT generator that builds an NFT collection with all metadata</h2>

This repository contains everything you need to generate images and metadata to be uploaded to blockchain as an NFT collection

The core function of creating the NFTs and meatadata requires use of the /Finished and /Layers folders (to contain the images) as well as the NFT-generator.py, config.py, and update-JSON-URI.py files.

The /Filename-assistant directory contains some code I wrote to expedite the process of taking attribute filenames and probabilities from a spreadsheet (.csv) and getting them into the format required for the config.py file. This is not necessary and if you don't have very many assets this will slow you down. If you have lots of assets, this will save you a ton of troubleshooting headache. Trust me.

Then I wrote the stats.py script to quickly see how the the probabilities actually expressed and to test nothing was going wrong. This is also not necessary to use for a smaller collection. I'd recommend using it for testing larger collection or if you just want to measure the precise rarity of each attribute.

I used this code successfully to create a 10,000 NFT collection that was then deployed onto the Polygon blockchain. The code for the smart contract and the web3 enabled website portions of this project will be added to separate repositories soon.

So how do you use this code?

<h2>IMAGES and PROBABILITIES</h2>

First thing is you need your layers and attributes. Make these in .png files with clear backgrounds. Order the layers (in the config + metadata) in the order you want them added to the NFT. ie. lowest number is the lowest layer, highest number is the highest layer. 

Then you need to decide how probable you want each attribute to be within it's layer. The probabilities of all the attributes within a layer MUST add up to 100. If you want there to be a chance there is no attribute in that layer, simply add a blank (clear) .png file to your attributes. The probability you assign that will be the probability there is no asset on that layer for any given NFT.

<h2>CONFIG</h2>

Once you have these probabilities decided, you need to get this information into your config.py file. You can enter this by hand or you can use the /Filename-assistant code. Up to you. 
First open the config.py file. There are currently 4 layers (4 dicts in the "layers" list). Copy/paste or cut the number of layers as you require. Edit "name" to be what you want the layer to be called in your metadata and on NFT exchanges. Make sure the path to the folder for this layer is correct (relative to this directory on your computer).
The text you put for each attribute file in the "filename" list must EXACTLY match the filename of the attribute image WITHOUT the file extension. ie. it the filename is "blue.png" you put "blue" as the item in that list. 
Then you enter the probability you have assigned to that attribute in the "weights" list. The items in the "filename" list are matched to their corresponding "weight" by index, so don't mess up the order.
The "values" list for a given layer is simply to be used if you want the name of the attribute to display differnetly in the metadata than the filename. I recommend keeping these the same. 

After configuring the config.py file you must adjust the metadata struct in the NFT-generator.py file (called "metadata") accordingly. Change the "description" to be relevant to your collection. Change the "external_url" to your website if you have one. Leave "image" blank. We will deal with that later.
Now change the number of dicts in the "attributes" list to match your number of layers. Rename each "trait_type" to your layer name.

I will add an explaination of the /Filename-assistant code later.

<h2>GENERATE</h2>

This part is pretty easy. Scroll down to the last line in the NFT-generator.py file and change the number 40 to however many NFTs you want in your collection. Be conscious of how many possible combinations you can have with your number of layers and attributes. The code will remove duplicates, so the code will keep attempting to make new combinations even if all possible combinations have been created. You've been warned.

Run the file. This could take a while.

<h2>UPLOAD TO IPFS AND UPDATE METADATA</h2>

So hopefully now you've got a beautiful new collection of computer generated images. The next part of this process assumes you are uploading these images and corresponding metadata to IPFS. I used Pinata so thats what I'm going to tell you to use too. If you don't know anything about this, neither did I before creating this NFT collection. It's pretty straight forward so don't worry.
If all you wanted was to make a bunch of images on your computer then congrats - you're done. I doubt thats the case though so let's move on.

Your NFT images should all be contained in the /Finished/img directory. This /img directory is what we are uploading to Pinata. So navigate over to https://www.pinata.cloud/
Create an account if necessary and upload your folder. This could also take a while. Once finished the folder will be visible in your dashboard. It will also have a unique CID. You need to copy this.

Now go back to your code editor and open the update-JSON-URI.py file. Find the variable "IPFS_URI" (on line 8 at the time of writing). Replace the "<yourCID>" portion of that variable with your CID. Do this EXACTLY or your NFT metadata won't be pointing to your NFT image file and the whole thing won't work.  Remember to leave the "/" after your CID.

After this, save the file and run it. you can check this worked by opening one of the JSON files in the /Finished/metadata directory. If the "image" value is something like this: "ipfs://QmR6rAmpcchWTNEvUY3fZ4bYJuwbBkYy1Wq37odKHa5QmK/231.png" the code worked.

Now we need to upload all this metadata to IPFS and Pinata as well. Navigate back to https://www.pinata.cloud/ and upload the /Finished/metadata directory. Again it could take a couple minutes. After finishing, this will also have a CID. This CID is what will be going in the Smart Contract to be put on blockchain.

Congrats on making it this far! Soon I will be uploading the next portion of this project - the Smart Contract.







