#importing the library
from PIL import Image
from sys import argv


#adding the path of the text file
filename = "cyber.txt"

#reading the file
try:
    txt = open(argv[1], "r")
except IndexError: 
    print("File not found")
    txt = open(filename, "r")
except FileNotFoundError:
    print("Could not find file, use default file")
    txt = open(filename, "r")

Bg = Image.open("data/bg.png")
sheet_width = Bg.width
space, ht = 0, 80

#reading the file and giving the paragraph height, width, and space 
for i in txt.read().replace("\n", ""):
    lc = Image.open("data/{}.png.".format(str(ord(i))))
    Bg.paste(lc, (space, ht))
    size = lc.width
    height = lc.height
    space+= size 

    if sheet_width < space or len(i)*35 > (sheet_width - space):
        space, ht = 0, ht+70
    print(space)
    print(sheet_width)
    #displaying file
    Bg.show()
    Bg.save("save.png")