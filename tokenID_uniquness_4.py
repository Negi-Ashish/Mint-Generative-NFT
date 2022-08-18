from generate_trait_3 import *;

all_images = generate_img_list()

# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)



# Add token Id to each image start from 1
def add_token_id():
    if(all_images_unique(all_images)):
        i = 1
        for item in all_images:
            item["tokenId"] = i
            i = i + 1
        
        return(all_images)
    else:
        raise("All images are not unique")