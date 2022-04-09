from components import vars
from PIL import Image

ironMan = Image.open("ironMan.jpg")
groot = Image.open("groot.jpg")
wWoman = Image.open("wWoman.jpg")

def total(value):
    if value < 0:
        vars.character = vars.characters[1]
        groot.show()
        print("It's " + vars.character)
    
    elif value >5000:
        vars.character = vars.characters[2]
        wWoman.show()
        print("It's " + vars.character)

    else:
        vars.character = vars.characters[0]
        ironMan.show()
        print("It's " + vars.character)
