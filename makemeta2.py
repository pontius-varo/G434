import os
import json

f = open('./metadata/all-traits.json')
data = json.load(f)

# Change Base URL and PROJECT_NAME when ready for production
# Your base URL should be the IPFS URL given by the service you uploaded your nft pics to
# This should be edited via json...
BASE_URL = "https://ipfs.io/ipfs/QmamdbvsfUCFQK7dvUfqWEqDrXHfPUSqRfQAs63Yg4Rugb/"
PROJECT_NAME = "PROTOMORPHS"


def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }


for i in data:

    token_id = i['tokenId']
    # IMMUTABLE X "STANDARD"
    token = {
        "name": PROJECT_NAME + ' ' + str(token_id),
        "image_url": BASE_URL + str(token_id) + '.png',
        "tokenId": token_id,
    }
    # THIS NEEDS TO BE AUTOMATED
    token["Canvas"] = i["A#Canvas"]
    token["Fur"] = i["B#Fur"]
    token["Tier"] = i["C#Tier"]
    token["Flair"] = i["D#Flair"]
    token["Eye"] = i["E#Eye"]
    token["Outfit"] = i["F#Outfit"]
    token["Bottoms"] = i["G#Bottoms"]
    token["Head"] = i["H#Head"]
    token["Wielding"] = i["I#Wielding"]
    token["Weather"] = i["J#Weather"]
    # OPTIONAL | Uncomment if your NFT has an animation

    with open('./metadata/' + str(token_id) + ".json", 'w') as outfile:
        json.dump(token, outfile, indent=4)

f.close()
