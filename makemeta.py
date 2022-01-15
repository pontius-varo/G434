import os
import json

f = open('./metadata/all-traits.json')
data = json.load(f)

# Change Base URL when ready for production
BASE_URL = "https://foo.net"
PROJECT_NAME = ""


def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }


for i in data:
    token_id = i['tokenId']
    token = {
        "image": BASE_URL + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    # Default face needs to be replaced
    token["attributes"].append(getAttribute("Background", i["Background"]))
    token["attributes"].append(getAttribute("Armor", i["Armor"]))
    token["attributes"].append(getAttribute("Acessory", i["Acessory"]))
    token["attributes"].append(getAttribute("RightArm", i["RightArm"]))
    token["attributes"].append(getAttribute("LeftArm", i["LeftArm"]))
    token["attributes"].append(getAttribute("Head", i["Head"]))
    token["attributes"].append({"Animation": "None"})

    with open('./metadata/' + str(token_id) + ".json", 'w') as outfile:
        json.dump(token, outfile, indent=4)

f.close()
