from tkinter import Tk
from tkinter.filedialog import FileDialog
import exifread
import pprint

Tk().withdraw()
f = FileDialog()

tags = exifread.process_file(f)
print(tags.keys())
pprint.pprint(tags)
f.close()