from PIL import Image
from IPython.display import display
import random
import os
import json


# Assign incompatible traits
incompatible_active = False
incompatible_traits = []

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
                #print(f'Enter weight value for key {key}')
                #key_weight = input("> ")
                key_weight = '10'
                # Add value as an interger
                key_weights.append(int(key_weight))

            weights.append(key_weights)

        # Catch any errors (especially if a user enters a character) and break
        except Exception as e:
            print(f'An error occured: {e}')
            break
    return weights

# Should take an object instead of two distinct arrays
# For example : INCOMPANTIBLE_TRAITS = {"RIGHTARM": ["TRIDENT", "SPEAR"], "LEFTARM": ["TRIDENT", "SPEAR"]}
# catchTraits should take the key, loop through the subarray and compare them
#  to the traits being passed through after image generation


def createIncompatibles():
    incomp = {}

    num = int(input(
        'Please enter the number of incompatible traits you have: '))

    x = 0

    while x < num:
        trait_key = input("Enter the base trait: ")
        num_of_incomps = int(input(
            f'How many incompatibles does trait {trait_key} have?: '))

        count = 0

        incomp_array = []

        # The Data struct for this needs to be changed.
        # the CATEGORY must be included somehow, as it will be used to FIND
        # an incompatible trait, which would be better than EXCLUDING an
        # entire category all together
        while count < num_of_incomps:
            incompatible_trait = input(
                f'Enter your incompatible category for {trait_key}: ')

            incomp_array.append(incompatible_trait)
            count += 1

        print(
            f'OK finshed adding {trait_key} with the following incompatible categories its: {incomp_array}')
        incomp[trait_key] = incomp_array
        x += 1

    return incomp


def catchIncompatibles(incompatible_obj, newimage, active):

    if(active):
        for trait in incompatible_obj:
            for category in newimage:
                if(newimage[category] == trait):
                    for incompatible in incompatible_obj[trait]:
                        if(newimage[incompatible] != "None"):
                            print(f'BEFORE {newimage}')
                            newimage[incompatible] = "None"
                            print("Incompatible found! Changing...")
                            print(f'AFTER {newimage}')
                        else:
                            print("Not!")

                else:
                    print("Pass!")

    return newimage


def newImage():

    # CHANGE IF YOU HAVE DIFFERENT CATEGORIES
    categories = ["Accessory", "Armor", "Background",
                  "Hat", "Head", "LeftArm", "RightArm"]
    new_image = {}

    for x in range(0, len(categories)):
        new_image[categories[x]] = random.choices(asset_keys[x], weights[x])[0]

    cleaned_image = catchIncompatibles(
        incompatible_traits, new_image, incompatible_active)

    if new_image in all_images:
        return newImage()
    else:
        return cleaned_image


def all_images_unique(image_set):
    seen = list()
    return not any(i in seen or seen.append(i) for i in image_set)


def addTokenID(image_set):
    # Add token Id to each image
    i = 0
    for item in image_set:
        item["tokenId"] = i
        i = i + 1

    return image_set


def finalizeImages(image_set):

    # Manual open_images for now, need to figure out a way to take the categories (from the file names)
    # and for each category create an REAL image_set
    for item in image_set:

        accessory_img = Image.open(
            f'./Assets/Accessories/{nft_assets[0][item["Accessory"]]}.png').convert('RGBA')

        armor_img = Image.open(
            f'./Assets/Armor/{nft_assets[1][item["Armor"]]}.png').convert('RGBA')

        background_img = Image.open(
            f'./Assets/Background/{nft_assets[2][item["Background"]]}.png').convert('RGBA')

        hat_img = Image.open(
            f'./Assets/Hats/{nft_assets[3][item["Hat"]]}.png').convert('RGBA')

        head_img = Image.open(
            f'./Assets/Heads/{nft_assets[4][item["Head"]]}.png').convert('RGBA')

        leftarm_img = Image.open(
            f'./Assets/LeftArm/{nft_assets[5][item["LeftArm"]]}.png').convert('RGBA')

        rightarm_img = Image.open(
            f'./Assets/RightArm/{nft_assets[6][item["RightArm"]]}.png').convert('RGBA')

        # Create each Composite | Stack Images on top of each other
        # Consider putting this into a for loop that creates a composite for each category
        comp1 = Image.alpha_composite(background_img, armor_img)
        comp2 = Image.alpha_composite(comp1, accessory_img)
        comp3 = Image.alpha_composite(comp2, rightarm_img)
        comp4 = Image.alpha_composite(comp3, leftarm_img)
        comp5 = Image.alpha_composite(comp4, head_img)
        comp6 = Image.alpha_composite(comp5, hat_img)

        # Convert to RGB
        rgb_im = comp6.convert('RGB')
        file_name = str(item["tokenId"]) + ".png"
        rgb_im.save("./images/" + file_name)

    METADATA_FILENAME = './metadata/all-traits.json'
    with open(METADATA_FILENAME, 'w') as outfile:
        json.dump(image_set, outfile, indent=4)


# SCRIPT STARTS HERE #

# Assemble assets from ./Assets
nft_assets = getAssets(path)

# Retrieve Asset keys from nft_assets
asset_keys = getAssetKeys(nft_assets)

# Assign weights to keys, prompt the user and have them give input
weights = getWeights(asset_keys)

# Prompt the User to retrive the amount of nfts to be generated
# [TODO] 'Catch' user errors (such as submiting a char) and reprompt them
print("Please give the numerical amount of nfts you want created")
total_images = int(input("> "))

if(input("Would you like to assign incompatible traits? (y/n)> ") == 'y'):
    incompatible_active = True
    incompatible_traits = createIncompatibles()
    print(incompatible_traits)
else:
    pass

# Leave nft image creation here
all_images = []

# Creates all new Images and adds them to all_images
for i in range(total_images):

    new_trait_image = newImage()

    all_images.append(new_trait_image)

print("Are all images unique?", all_images_unique(all_images))

all_images_with_ids = addTokenID(all_images)

finalizeImages(all_images_with_ids)
