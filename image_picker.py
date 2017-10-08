import json
from random import randint
import asyncio

class ImagePicker():
    """Methods and settings related to random selection of images."""
    def __init__(self):
        # Create a dictionary with separate history lists per command.
        self.image_history = {"shroom_history": [], "walrus_history": []}
        # Load .json file with image history.
        try:
            with open('image_history.json') as f_obj:
                self.image_history = json.load(f_obj)
        except FileNotFoundError:
            print("Image history not found.")
            
    
    async def select_image(self, folder, num_pictures):
        """
        Generate address for image dynamically. Needs subfolder name and
        number of pictures in subfolder arguments. Will keep a list of the last
        10 images picked and save it to .json history file, reroll if selected
        pic is in the history file.
        """
        history_folder = eval("self.image_history['" + folder + "_history']")
        pic_num = randint(1, num_pictures)
        while pic_num in history_folder:
            pic_num = randint(1, num_pictures)
        history_folder.append(pic_num)

        # history folder only keeps last 10 images.
        if len(history_folder) > 10:
            del history_folder[0]
            
        # write image history to .json file after final image selection.
        with open('image_history.json', 'w') as f_obj:
            json.dump(self.image_history, f_obj)
            
        image_path = "images/" + folder + "/" + str(pic_num) + ".jpg"
        return image_path
