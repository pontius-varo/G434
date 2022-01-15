from PIL import Image
from IPython.display import display
import random
import os
import json


path = './Assets/'


def getAssets(path):
    filedict = []

    for root, dirs, files in sorted(os.walk(path)):
        new_obj = {}
        for file in files:
            key = file.partition("#")[0]
            file = file.partition(".")[0]

            new_obj[key] = file

        filedict.append(new_obj)

    # Clean empty obj
    filedict.pop(0)
    return filedict


def getAssetKeys(array):

    mykeys = []
    for item in nft_assets:
        newarray = []
        for key in item:
            newarray.append(key)

        mykeys.append(newarray)

    return mykeys


# Retrieve Asset objects based on files in ./Assets
nft_assets = getAssets(path)

# For now, assign them to variables
accessory_files = nft_assets[0]
armor_files = nft_assets[1]
background_files = nft_assets[2]
hat_files = nft_assets[3]
head_files = nft_assets[4]
left_arm_files = nft_assets[5]
right_arm_files = nft_assets[6]

# Retrieve Asset keys
asset_keys = getAssetKeys(nft_assets)

# Assign weights to keys, prompt the user and have them give input
