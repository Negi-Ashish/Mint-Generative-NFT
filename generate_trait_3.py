from trait_rarity_1 import *;

## Generate Traits
TOTAL_IMAGES = 10 # Number of random unique images we want to generate


all_images = [] 
# A recursive function to generate unique image combinations
def create_new_image():
    
    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["Face"] = random.choices(face, face_weights)[0]
    new_image ["Ears"] = random.choices(ears, ears_weights)[0]
    new_image ["Eyes"] = random.choices(eyes, eyes_weights)[0]
    new_image ["Hair"] = random.choices(hair, hair_weights)[0]
    new_image ["Mouth"] = random.choices(mouth, mouth_weights)[0]
    new_image ["Nose"] = random.choices(nose, nose_weights)[0]
    new_image ["Accessories"] = random.choices(access, access_weights)[0]
    
    if new_image in all_images:
        return create_new_image()
    else:
        return new_image
    
    
# Generate the unique combinations based on trait weightings
def generate_img_list():

    for i in range(TOTAL_IMAGES): 
        
        new_trait_image = create_new_image()
        
        all_images.append(new_trait_image)
    # print(all_images)
    return all_images

# generate_img_list()

# example of result
#[
#   {
#     'Face': 'White',
#     'Ears': 'No Earring',
#     'Eyes': 'Regular',
#     'Hair': 'Mohawk',
#     'Mouth': 'Red Lipstick',
#     'Nose': 'Nose'
#   },
#   {
#     'Face': 'White',
#     'Ears': 'Right Earring',
#     'Eyes': 'Regular',
#     'Hair': 'Red Mohawk',
#     'Mouth': 'Teeth Smile',
#     'Nose': 'Nose'
#   },
#   {
#     'Face': 'Black',
#     'Ears': 'Left Earring',
#     'Eyes': 'Rayban',
#     'Hair': 'Bald',
#     'Mouth': 'Big Smile',
#     'Nose': 'Nose'
#   },
#   {
#     'Face': 'Black',
#     'Ears': 'Right Earring',
#     'Eyes': 'Small',
#     'Hair': 'Red Mohawk',
#     'Mouth': 'Teeth Smile',
#     'Nose': 'Nose'
#   },
#   {
#     'Face': 'Black',
#     'Ears': 'Left Earring',
#     'Eyes': 'Focused',
#     'Hair': 'Red Mohawk',
#     'Mouth': 'Black Lipstick',
#     'Nose': 'Nose'
#   }
#]