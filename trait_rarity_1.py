from PIL import Image 
from IPython.display import display 
import random
import json
import os

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

face = ["White", "Black"]
face_weights = [6, 4]

ears = ["No Earring", "Left Earring", "Right Earring", "Two Earrings"]
ears_weights = [2, 3, 4, 1]

eyes = ["Regular", "Small", "Rayban", "Hipster", "Focused"]
eyes_weights = [4, 2, 1, 1, 2]

hair = ['Up Hair', 'Down Hair', 'Mohawk', 'Red Mohawk', 'Orange Hair', 'Bubble Hair', 'Emo Hair',
 'Thin Hair',
 'Bald',
 'Blonde Hair',
 'Caret Hair',
 'Pony Tails']
hair_weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

mouth = ['Black Lipstick', 'Red Lipstick', 'Big Smile', 'Smile', 'Teeth Smile', 'Purple Lipstick']
mouth_weights = [2, 2, 2, 2, 1, 1]

nose = ['Nose', 'Nose Ring']
nose_weights = [8, 2]

access = ["Cigarette","Sigaar"]
access_weights = [9,1]