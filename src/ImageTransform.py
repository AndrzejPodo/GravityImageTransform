import math
from PIL import Image
#image - img to transform, v0 - initial velocity, a - acceleration, T - period between lines, water_screen_size - size of screen in cm
def transform_image(image, v0, a, T, water_screen_size):
    img = Image.open(image)

    # D0 = int(distance(0, v0, a, T)*100) #length of first chunk in [cm]
    #resizing to water screen heigth but we multiply by 100 to increase resolution before tranforming
    h0 = 10 #[cm]
    baseheigth = water_screen_size[1] #cm
    hpercent = (baseheigth/float(img.size[1]))
    wsize = int((float(img.size[0])*float(hpercent)))
    img = img.resize((wsize,baseheigth*100), Image.ANTIALIAS)

    img_layers = []
    for i in range(int(baseheigth/h0)):
        box = (0,h0*i*100,wsize, h0*(i+1)*100)
        img_layers.append(img.crop(box))
    
    dest = None
    for i in range(1, len(img_layers)+1):
        w = img_layers[i-1].width
        h = int(img_layers[i-1].height*ratio(0.01*baseheigth/2, i*h0*0.01, v0, a))
        if dest:
            dest = get_concat(dest, img_layers[i-1].resize((w,h), Image.ANTIALIAS))
        else:
            dest = img_layers[i-1]

    dest.resize((dest.width, int(dest.height/100))).save("./src/arrow_tranformed.png")

def distance_gain(x, v0, a, T):
    return T*a/math.sqrt(v0**2 + 2*a*x)

def ratio(x1, x2, v0, a):
    vn = v(x2, v0, a)
    v1 = v(x1, v0, a)
    return (v0+v1)/(2*vn-v1+v0)

def v(x, v0, a):
    return math.sqrt(v0**2 + 2*a*x)

def distance(x, v0, a, T):
    return T*(math.sqrt(v0**2 + 2*a*x) + 0.5*a*T)

def get_concat(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

transform_image("./src/arrow.png", 5,20,0.02,(264,192))
