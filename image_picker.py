from random import randint
import asyncio

class ImagePicker():
    """Methods and settings related to random selection of images."""
    def __init__(self):
        self.shroom_history, self.walrus_history = [], []
    
    async def select_image(self, folder, num_pictures):
        """
        Generate address for image dynamically. Needs subfolder name and
        number of pictures arguments
        """
        self.history_folder_name = folder + "_history"
        self.history_folder = getattr(self, self.history_folder_name)
        pic_num = randint(1, num_pictures)
        while pic_num in self.history_folder:
            pic_num = randint(1, num_pictures)
        else:
            self.history_folder.append(pic_num)
        if len(self.history_folder) > 10:
            del self.history_folder[0]
        image_path = "images/" + folder + "/" + str(pic_num) + ".jpg"
        return image_path
