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


def getWeights(keys):
    # Create an empty array to export weights
    weights = []
    # Loop through each key array
    for key_array in keys:
        # Create another empty array to organize weights
        key_weights = []
        try:
            # For each key in the key array
            for key in key_array:
                # Ask the user to give a weight value
                print(f'Enter weight value for key {key}')
                key_weight = input("> ")
                # Add value as an interger
                key_weights.append(int(key_weight))

            weights.append(key_weights)

        # Catch any errors (especially if a user enters a character) and break
        except Exception as e:
            print(f'An error occured: {e}')
            break
    return weights


# This script returns all the asset arrays from the subdirectories in Alphabetical order
# Therefore, instead of assigning all values to different variables, we can just retrieve them from the array returned

# in this case where we have the following subdirectories in ./Assets
# [Accesories, Armor, Background, Hat, Head, LeftArm, RightArm]
# getAssets returns the following Objects with key value pairs {"shortened-key" : "file.extension"}
# [{Accesories}, {Armor}, {Background}, {Hat}, {Head}, {LeftArm}, {RightArm}]
# From those assets we retrieve the keys created using getAssetKeys
# those keys are then consumed by getWeights, which after prompting the user to assign
# a weight to each key, returns an array of weight arrays in a similar order to getAssets ~>
# [[Accessory_weights], [Armor_weights], [Background_weights], [Hat_weights], [Head_weights], [LeftArm_weights], [RightArm_weights]]
# Therefore instead of creating specific arrays for a fixed number of categories, we can create them dynamically
# As a result, when it is time to assemble the nft, we can simply interate through first the nft_assets array and then
# the weights array to establish rarity

# Retrieve Asset objects based on files in ./Assets
nft_assets = getAssets(path)

# Retrieve Asset keys
asset_keys = getAssetKeys(nft_assets)

# Assign weights to keys, prompt the user and have them give input
weights = getWeights(asset_keys)

# Prompt the User to retrive the amount of nfts to be generated
print("Please give the numerical amount of nfts you want created")
total_images = int(input("> "))

# Assign incompatible traits

# Leave incompatible traits funciton here

# Leave nft image creation here
