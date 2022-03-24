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

# Returns category array based on subdirectories in assets


def getCategories(path):
    categories = sorted(os.walk(path))[0][1]

    # "sorted" ensures that they will be returned alphabetically
    return sorted(categories)


# CHANGE IF YOU HAVE DIFFERENT CATEGORIES
categories = getCategories(path)
#print(categories)


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
                print(key_array)
                # Ask the user to give a weight value
                # print(f'Enter weight value for key {key}')
                # key_weight = input("> ")
                print("default weight of 1 set")
                key_weight = '1'
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
# Should be: INCOMPATIBLE_TRAITS = {"MYTRAIT": ["TRAIT", "Trait"], "MYTRAIT": ["TRAIT", "Trait"]}
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
            f'OK finshed adding {trait_key} with the following incompatible categories : {incomp_array}')
        incomp[trait_key] = incomp_array
        x += 1

    return incomp


def catchIncompatibles(incompatible_obj, newimage, active):

    # INCOMPATIBLE_TRAITS = {"MYTRAIT": ["TRAIT", "Trait"], "MYTRAIT": ["TRAIT", "Trait"]}

    if(active):
        # for each 'key' in incompatible_obj
        for trait in incompatible_obj:
            # for each 'key' in newimage object
            for category in newimage:
                # if newimage[category] ((VALUE)) == trait
                if(newimage[category] == trait):
                    # for value in array (incompatible_obj[trait])
                    for incompatible in incompatible_obj[trait]:
                        if(newimage[category] == incompatible):
                            print(f'BEFORE {newimage}')
                            newimage[category] = "None"
                            print("Incompatible found! Changing...")
                            print(f'AFTER {newimage}')
                        else:
                            print("Not!")

                else:
                    print("Pass!")

    return newimage


def newImage():

    # # CHANGE IF YOU HAVE DIFFERENT CATEGORIES
    # categories = getCategories(path)
    new_image = {}

    for x in range(0, len(categories)):
        new_image[categories[x]] = random.choices(asset_keys[x], weights[x])[0]

    cleaned_image = catchIncompatibles(
        incompatible_traits, new_image, incompatible_active)

    if new_image in all_images:
        return newImage()
    else:
        print(cleaned_image)
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
    # This has been handled

    # Potentially, this can be fixed as follows
    # for each category in categories & asset_num < nft_assets length
    # name = category + '_img'
    # data[name] = Image.open(f'./Assets/{category}/{nft_assets[asset_num][item[sub_category]]}.png').convert('RGBA')
    # then for each key in data
    # compile all images
    # Convert to RGBA and export

    for item in image_set:
        asset_num = 0

        assembled_image = []

        for category in categories:

            img_part = Image.open(
                f'./Assets/{category}/{nft_assets[asset_num][item[category]]}.png').convert('RGBA')

            asset_num = asset_num + 1
            assembled_image.append(img_part)

        def compile_images(composite_1, composite_2):

            return Image.alpha_composite(composite_1, composite_2)

        # Final composite base is always first two images
        final_composite = compile_images(
            assembled_image[0], assembled_image[1])

        for x in range(2, len(assembled_image)):

            final_composite = compile_images(
                final_composite, assembled_image[x])

        # Convert to RGB
        rgb_im = final_composite.convert('RGB')
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

#print(all_images_with_ids)

finalizeImages(all_images_with_ids)
