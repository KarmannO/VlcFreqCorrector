from PIL import Image
import numpy as np

class ImageLoader:
    @staticmethod
    def LoadImage3ub(filename):
        img = Image.open(filename).convert('RGB')
        return img.size[0], img.size[1], np.array(img.getdata())

    @staticmethod
    def LoadImage4ub(filename):
        img = Image.open(filename).convert('RGBA')
        return img.size[0], img.size[1], np.array(img.getdata())

    @staticmethod
    def LoadImage3f(filename):
        img = Image.open(filename).convert('RGB')
        return img.size[0], img.size[1], np.array(img.getdata()) / 255.0

    @staticmethod
    def LoadImage4f(filename):
        img = Image.open(filename).convert('RGBA')
        return img.size[0], img.size[1], np.array(img.getdata()) / 255.0

    @staticmethod
    def LoadImage1f(filename):
        img = Image.open(filename).convert('L')
        return img.size[0], img.size[1], np.array(img.getdata()) / 255.0

    @staticmethod
    def SaveImage3ub(filename, data, w, h):
        img = Image.new('RGB', [w, h])
        img.putdata(data)
        img.save(filename)

    @staticmethod
    def SaveImage4ub(filename, data, w, h):
        img = Image.new('RGBA', [w, h])
        img.putdata(data)
        img.save(filename)

    @staticmethod
    def SaveImage3f(filename, data, w, h):
        img = Image.new('RGB', [w, h])
        new_d = data * 255.0
        formatted = []
        for el in new_d:
            formatted.append((int(el[0]), int(el[1]), int(el[2])))
        img.putdata(formatted)
        img.save(filename)

    @staticmethod
    def SaveImage4f(filename, data, w, h):
        img = Image.new('RGBA', [w, h])
        new_d = data * 255.0
        formatted = []
        for el in new_d:
            formatted.append((int(el[0]), int(el[1]), int(el[2])))
        img.putdata(formatted)
        img.save(filename)

    @staticmethod
    def SaveImage1f(filename, data, w, h):
        img = Image.new('F', [w, h])
        img.putdata(data * 255.0)
        img.convert('RGB').save(filename)