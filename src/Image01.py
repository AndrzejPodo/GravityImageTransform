from PIL import Image
import numpy as np

class Image01:
    def __init__(self, image):
        self.img_01 = Image.open(image).convert('1').resize((100,100))
        self.array01 = np.array(self.img_01.getdata()).reshape(self.img_01.size[0], self.img_01.size[1])
        self.array01[self.array01 <= 128 ] = 0
        self.array01[self.array01 > 128] = 1
        np.savetxt("foo.csv", self.array01, fmt="%i",delimiter=",")
