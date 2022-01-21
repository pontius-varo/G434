# G434 (Gaea)

A python script commissioned to create a set of NFTs with metadata

Requires the following libraries: PIL, IPython


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
