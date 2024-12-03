

import os


def list_directories(path):
    # List all items in the directory
    all_items = os.listdir(path)
    # Filter only directories
    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    return directories

