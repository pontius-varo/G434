import os
import json

f = open('./metadata/all-traits.json')
data = json.load(f)

# Change Base URL and PROJECT_NAME when ready for production
# Your base URL should be the IPFS URL given by the service you uploaded your nft pics to
# This should be edited via json...
BASE_URL = "https://ipfs.io/ipfs/QmamdbvsfUCFQK7dvUfqWEqDrXHfPUSqRfQAs63Yg4Rugb/"
PROJECT_NAME = "PROTOKNIGHTS"


def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }


for i in data:
    token_id = i['tokenId']
    token = {
        # For pinata, you need a backslash!
        "image": BASE_URL + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    # Default face needs to be replaced
    token["attributes"].append(getAttribute("Background", i["Background"]))
    token["attributes"].append(getAttribute("Armor", i["Armor"]))
    token["attributes"].append(getAttribute("Accessory", i["Accessory"]))
    token["attributes"].append(getAttribute("RightArm", i["RightArm"]))
    token["attributes"].append(getAttribute("LeftArm", i["LeftArm"]))
    token["attributes"].append(getAttribute("Head", i["Head"]))
    # OPTIONAL | Uncomment if your NFT has an animation
    token["attributes"].append({"Animation": "None"})

    with open('./metadata/' + str(token_id) + ".json", 'w') as outfile:
        json.dump(token, outfile, indent=4)

f.close()
