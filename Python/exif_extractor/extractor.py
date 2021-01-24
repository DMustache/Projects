from tkinter import Tk
from tkinter.filedialog import FileDialog
import exifread
import pprint

Tk().withdraw()
f = open('Python\exif_extractor\thumb_630.jpg')

tags = exifread.process_file(f)
print(tags.keys())
pprint.pprint(tags)
f.close()