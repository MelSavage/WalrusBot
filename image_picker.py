import json
from random import randint
import asyncio

class ImagePicker():
    """Methods and settings related to random selection of images."""
    def __init__(self):
        # Create a dictionary with separate history lists per command.
        self.shroom_history, self.walrus_history = [], []
        self.image_history = {}
        self.image_history["shroom_history"] = self.shroom_history
        self.image_history["walrus_history"] = self.walrus_history
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
        self.history_folder_name = "self.image_history['" + folder + "_history']"
        self.history_folder = eval(self.history_folder_name)
        pic_num = randint(1, num_pictures)
        while pic_num in self.history_folder:
            pic_num = randint(1, num_pictures)
        else:
            self.history_folder.append(pic_num)
        if len(self.history_folder) > 10:
            del self.history_folder[0]
        with open('image_history.json', 'w') as f_obj:
            json.dump(self.image_history, f_obj)
        image_path = "images/" + folder + "/" + str(pic_num) + ".jpg"
        return image_path
