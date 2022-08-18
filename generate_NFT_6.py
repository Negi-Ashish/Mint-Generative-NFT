#### Generate Images
from trait_rarity_1 import *;
from assign_trait_files_2 import *;
from trait_count_5 import *;
import pickle

# print(all_images)


os.mkdir(f'./generated-nft')

for item in all_images:

    im1 = Image.open(f'./face_parts/face/{face_files[item["Face"]]}.png').convert('RGBA')
    im2 = Image.open(f'./face_parts/eyes/{eyes_files[item["Eyes"]]}.png').convert('RGBA')
    im3 = Image.open(f'./face_parts/ears/{ears_files[item["Ears"]]}.png').convert('RGBA')
    im4 = Image.open(f'./face_parts/hair/{hair_files[item["Hair"]]}.png').convert('RGBA')
    im5 = Image.open(f'./face_parts/mouth/{mouth_files[item["Mouth"]]}.png').convert('RGBA')
    im6 = Image.open(f'./face_parts/nose/{nose_files[item["Nose"]]}.png').convert('RGBA')
    im7 = Image.open(f'./face_parts/access/{access_files[item["Accessories"]]}.png').convert('RGBA')

    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)
    com5 = Image.alpha_composite(com4, im6)
    com6 = Image.alpha_composite(com5, im7)

                     

    #Convert to RGB
    rgb_im = com6.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./generated-nft/" + file_name)


with open("test", "wb") as fp:
    pickle.dump(all_images, fp)