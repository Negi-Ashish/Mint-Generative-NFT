import os;
import json;
import pickle

with open("test", "rb") as fp:   # Unpickling
        meta_data = pickle.load(fp)


# print(meta_data)

### Generate Metadata for all Traits 
os.mkdir(f'./metadata')

METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(meta_data, outfile, indent=4)


#### Generate Metadata for each Image    

f = open('./metadata/all-traits.json',) 
data = json.load(f)

# Changes this IMAGES_BASE_URL to yours 
IMAGES_BASE_URL = "https://gateway.pinata.cloud/ipfs/QmP3FVh1JpQfpahkLMMwVToCuT8jmJggDT3BHrgXkSgQXi/"
PROJECT_NAME = "NFT_CREATOR"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }
for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_BASE_URL + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    token["attributes"].append(getAttribute("Face", i["Face"]))
    token["attributes"].append(getAttribute("Ears", i["Ears"]))
    token["attributes"].append(getAttribute("Eyes", i["Eyes"]))
    token["attributes"].append(getAttribute("Hair", i["Hair"]))
    token["attributes"].append(getAttribute("Mouth", i["Mouth"]))
    token["attributes"].append(getAttribute("Nose", i["Nose"]))
    token["attributes"].append(getAttribute("Accessories", i["Accessories"]))

    with open('./metadata/' + str(token_id) + ".json", 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()