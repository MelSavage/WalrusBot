import shelve, asyncio, os
from random import choice

class ImagePicker():
    """Methods and settings related to random selection of images."""
    def __init__(self):
        history_shelf = shelve.open("image_shelf")
        self.history_dict = {"shroom": [], "walrus": []}
        for key in history_shelf.keys():
            try:
                self.history_dict[key] = history_shelf[key]
            except KeyError:
                print("No history found for " + key + ".")
        history_shelf.close()

    async def select_image(self, folder):
        """
        Generate address for image dynamically. Needs subfolder name as
        arugment. Will keep a history list for each folder totaling
        one-third the number of images in the folder.
        """
        image_list = os.listdir(".\\images\\" + folder)
        selected_image = choice(image_list)
        while selected_image in self.history_dict[folder]:
            selected_image = choice(image_list)
        self.history_dict[folder].append(selected_image)

        # History folder keeps one third of the contents of the folder.
        history_amount = int(len(image_list)/3)
        print("History amount for " + folder + ". " + str(history_amount))
        while len(self.history_dict[folder]) > history_amount:
            del self.history_dict[folder][0]

        # Write image history to shelf file.
        history_shelf = shelve.open("image_shelf")
        try:
            history_shelf[folder] = self.history_dict[folder]
        except KeyError:
            print("No history saved for " + key + ".")
        history_shelf.close()

        image_path = ".\\images\\" + folder + "\\" + selected_image
        return image_path
