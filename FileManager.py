import os
import shutil

# Directory names
IMAGE_DIR = "/IMAGES/"
SVG_DIR = "/SVG/"
SCREENSHOTS_DIR = "/SCREENSHOTS/"
MUSIC_DIR = "/MUSIC/"
VIDEOS_DIR = "/VIDEOS/"
DOCS_DIR = "/DOCS/"
APPLICATIONS_DIR = "/APPLICATIONS/"
ARCHIVE_DIR = "/ARCHIVE/"

# Directory list
DIRECTORIES = [
    IMAGE_DIR, SVG_DIR, SCREENSHOTS_DIR, MUSIC_DIR,
    VIDEOS_DIR, DOCS_DIR, APPLICATIONS_DIR, ARCHIVE_DIR
]

# File extenions
IMAGE_EXT = ["png", "jpg", "jpeg", "gif", "jfif"]
SVG_EXT = ["svg"]
SCREENSHOT_EXT = ["greenshot"]
MUSIC_EXT = ["mp3"]
VIDEO_EXT = ["mp4"]
DOCS_EXT = ['doc', 'docx', 'odt', 'pdf', 'xls', 'xlsx', 'ods', 'ppt', 'pptx', 'txt']
APPLICATION_EXT = ["exe", "msi"]
ARCHIVE_EXT = ["zip", "rar"]

# Current directory
PATH = os.path.dirname(__file__)

# Shorthand functions
exists = lambda p: os.path.exists(p)
listdir = lambda p: os.listdir(p)
get_extension = lambda f: f.split(".")[-1].lower()
move_file = lambda file_, dir_: shutil.move(PATH + "/" + file_, PATH + dir_ + file_)

# shutil.move(PATH + "/" + file, PATH + ARCHIVE_DIR + file)


# Iterate over all the files in the present directory
FILES = listdir(PATH)


def make_directories():
    for DIR in DIRECTORIES:
        if not exists(PATH + DIR):
            os.mkdir(PATH + DIR)


# Make necessary directories before moving forward
make_directories()


def organize_files():
    for file in FILES:
        if get_extension(file) in IMAGE_EXT:
            if "Greenshot" in file:
                move_file(file, SCREENSHOTS_DIR)
            else:
                move_file(file, IMAGE_DIR)

        if get_extension(file) in MUSIC_EXT:
            move_file(file, MUSIC_DIR)

        if get_extension(file) in VIDEO_EXT:
            move_file(file, VIDEOS_DIR)

        if get_extension(file) in DOCS_EXT:
            move_file(file, DOCS_DIR)

        if get_extension(file) in APPLICATION_EXT:
            move_file(file, APPLICATIONS_DIR)

        if get_extension(file) in ARCHIVE_EXT:
            move_file(file, ARCHIVE_DIR)

        if get_extension(file) in SVG_EXT:
            move_file(file, SVG_DIR)


organize_files()
