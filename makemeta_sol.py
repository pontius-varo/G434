import os
import json
from dotenv import load_dotenv

# Load Local Traits
f = open('./metadata/all-traits.json')
data = json.load(f)

# Import from .env
load_dotenv()
# Change Base URL and PROJECTNAME in .env when ready for production
# Your base URL should be the IPFS URL given by the service you uploaded your nft pics to

base_url = os.getenv('BASEURL')
project_name = os.getenv('PROJECTNAME')
project_name_short = os.getenv('NFTSHORTHAND')
symbol = os.getenv('SYMBOL')
description = os.getenv('DESCRIPTION')

creator_address = os.getenv('CREATORADDRESS')
amount_shared = os.getenv('SHARED')


def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }


for i in data:
    token_id = i['tokenId']
    token = {
        # For pinata, you need a backslash!
        "name": project_name_short,
        "symbol": symbol,
        "description": description,
        "image": str(token_id) + '.png',
        "attributes": [],
        "properties": {
            "creators": [{"address": creator_address, "share": amount_shared}],
            "files": [{"uri": str(token_id) + '.png', "type": "image/png"}],
            "collection": {"name": project_name, "family": project_name}
        }
    }
    # # Default face needs to be replaced
    # token["attributes"].append(getAttribute("Background", i["Background"]))
    token["attributes"].append(getAttribute("Background", i["Background"]))
    token["attributes"].append(getAttribute("Clothes", i["Clothes"]))
    token["attributes"].append(getAttribute("Head", i["Head"]))
    token["attributes"].append(getAttribute("Vision", i["Vision"]))
    token["attributes"].append(getAttribute("Extra", i["Extra"]))

    with open('./metadata/' + str(token_id) + ".json", 'w') as outfile:
        json.dump(token, outfile, indent=4)

f.close()
