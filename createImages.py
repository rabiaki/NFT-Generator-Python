from PIL import Image
import os
import json
from json import JSONEncoder



class File:
    def __init__(self, uri, type):
        self.uri = uri
        self.type = type

class Properties:
    def __init__(self, files):
        self.files = files

class Attribute:
    def __init__(self, trait_type, value):
        self.trait_type = trait_type
        self.value = value

class Root:
    def __init__(self, image, name, description, external_url, seller_fee_basis_points, properties, attributes):
        self.image = image
        self.name = name
        self.description = description
        self.external_url = external_url
        self.seller_fee_basis_points = seller_fee_basis_points
        self.properties= properties
        self.attributes = attributes


class ClassEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__


def getPNGFiles(dirr):
    filelist= [file for file in os.listdir(dirr) if file.endswith('.png')]
    return filelist


def nftGenerator(main_address):
    im_base = Image.open(main_address +'/base.png')
    w, h = im_base.size

    assesstAddress = main_address + '/assets'
    colorAddress = main_address + '/colors'
    assesstList = getPNGFiles(assesstAddress)
    colorList = getPNGFiles(colorAddress)

    k = 1
    for ass in assesstList:
        ass_img = Image.open(assesstAddress + "/" + ass)

        for color in colorList:
            name = "nft" + str(k)

            with open(main_address +"/results/"+ name + '.json', 'w') as f:
                color_img = Image.open(colorAddress + "/" + color)

                imageName = main_address + "/results/"  + name + ".png"
                img = Image.new("RGBA", im_base.size)

                img.paste(color_img, (0,0), color_img)
                img.paste(im_base, (0,0), im_base)
                img.paste(ass_img, (0,0), ass_img)
                img.save(imageName, "PNG")

                file = File(imageName, "image/png")
                prop = Properties([file])

                attr1 = Attribute("background", color.split(".")[0])
                attr2 = Attribute("asset", ass.split(".")[0])

                r = Root(name+".png", "name", "description", "", 0,  prop, [attr1, attr2])

                k += 1

                json.dump(r.__dict__, f, indent=4, cls=ClassEncoder)


#main_address = "F:/PhD/KAIST Computing School/images"
#nftGenerator(main_address)



