# G434 (Gaea)

A python script that creates a set of NFTs with metadata, along with adding in customization for the user. Based mostly on Edward Jones' own script, which you can find here:'https://betterprogramming.pub/create-your-own-nft-collection-with-python-82af40abf99f'

Requires the following libraries: PIL, IPython


## 1.3 Changelog
* Created finalizeImages function, which assembles all images in the array passed through and dumps the data from that array into a json file
* Added all_images_unique function to verify if all images generated are unique
* Added "Animation" key to "attributes" in token mapping

## 1.2 ChangeLog
* Created createIncompatibles, catchIncompatibles, newImage functions
* Added incompatible_active variable to determine whether or not to look for incompatibles
* Added default categories to newImage function (Will be changed in the future!)
## 1.1 ChangeLog
* Created getWeights function to prompt user for weights and store those values in a returned array
* Created total_images variable where user prompt for nft amount given by user is stored

## 1.0 ChangeLog
* Created function getAssets to retrieve an array of objects with certain values based on  the ./Assets directory
* Created function getAssetKeys to retrieve keys from each object in the getAssets array
