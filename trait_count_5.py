from trait_rarity_1 import *;
from tokenID_uniquness_4 import add_token_id;

# set trait count of all trait to zero first

face_count = {}
for item in face:
    face_count[item] = 0
    
ears_count = {}
for item in ears:
    ears_count[item] = 0

eyes_count = {}
for item in eyes:
    eyes_count[item] = 0
    
hair_count = {}
for item in hair:
    hair_count[item] = 0
    
mouth_count = {}
for item in mouth:
    mouth_count[item] = 0
    
nose_count = {}
for item in nose:
    nose_count[item] = 0

access_count = {}
for item in access:
    access_count[item] = 0

all_images = add_token_id()

def rarity():
    for image in all_images:
        face_count[image["Face"]] += 1
        ears_count[image["Ears"]] += 1
        eyes_count[image["Eyes"]] += 1
        hair_count[image["Hair"]] += 1
        mouth_count[image["Mouth"]] += 1
        nose_count[image["Nose"]] += 1
        access_count[image["Accessories"]] += 1

    print(face_count)
    print(ears_count)
    print(eyes_count)
    print(hair_count)
    print(mouth_count)
    print(nose_count)
    print(access_count)

rarity()