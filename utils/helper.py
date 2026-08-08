import os
import time


def create_folder(path):

    if not os.path.exists(path):
        os.makedirs(path)


def current_time():

    return time.strftime("%Y-%m-%d %H:%M:%S")


def image_name():

    return str(int(time.time() * 1000)) + ".jpg"