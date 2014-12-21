import math
from PIL import Image 


img = Image.new( 'RGB', (256,276), "white") # create a new black image
pixels = img.load() # create the pixel map
 
#for i in range(img.size[0]):    # for every pixel:
#    for j in range(img.size[1]):
         # set the colour accordingly
 
def single (i):
    return math.sin((i / 256.0) * 2. * math.pi)
    
def wave_shape(x):
    #shape it, a is amount, smaller is more square
    a = .1
    
    if x == 0:
        y = 0
    if x > 0:
        if x < a: 
            y = x
        if x > a: 
            y = a + (x-a)/(1 + ( ((x-a)/(1-a)) * ((x-a)/(1-a)) ) )
        if x > 1: 
            y = (a+1)/2
    if x < 0:
        x *= -1
        if x < a: 
            y = x
        if x > a: 
            y = a + (x-a)/(1 + ( ((x-a)/(1-a)) * ((x-a)/(1-a)) ) )
        if x > 1: 
            y = (a+1)/2
        y *= -1;
        
    #normalize it
    y = y * (1/((a+1)/2))
    return y

def single_shaped (i):
    x = math.sin((i / 256.0) * 2. * math.pi)
    return wave_shape(x)

def seven_descending (i):
    sin1 = math.sin((i / 256.0) * 2. * math.pi) * .1
    sin2 = math.sin((i / 256.0) * 2. * math.pi * 2.0) * .2
    sin3 = math.sin((i / 256.0) * 2. * math.pi * 3.0) * .3
    sin4 = math.sin((i / 256.0) * 2. * math.pi * 4.0) * .4
    sin4 = math.sin((i / 256.0) * 2. * math.pi * 5.0) * .5
    sin4 = math.sin((i / 256.0) * 2. * math.pi * 6.0) * .6
    sin4 = math.sin((i / 256.0) * 2. * math.pi * 7.0) * .7
    val = (sin1 + sin2 + sin3 + sin4) / 2.8
    return val

def seven_all_on (i):
    sin1 = math.sin((i / 256.0) * 2. * math.pi)
    sin2 = math.sin((i / 256.0) * 2. * math.pi * 2.0)
    sin3 = math.sin((i / 256.0) * 2. * math.pi * 3.0)
    sin4 = math.sin((i / 256.0) * 2. * math.pi * 4.0)
    sin4 = math.sin((i / 256.0) * 2. * math.pi * 5.0)
    sin4 = math.sin((i / 256.0) * 2. * math.pi * 6.0)
    sin4 = math.sin((i / 256.0) * 2. * math.pi * 7.0)
    val = (sin1 + sin2 + sin3 + sin4) / 3
    return wave_shape(val)
    
def one_five_oct(i) :
    sin1 = math.sin((i / 256.0) * 2. * math.pi)
    sin2 = math.sin((i / 256.0) * 2. * math.pi * 2.0)
    sin3 = math.sin((i / 256.0) * 2. * math.pi * 3.0)
    val = (sin1 + sin2 + sin3) / 3
    return val
    


# we go from -1 to 258 cause we need some bookends for the interpolation
for i in range(-1,258):
    #val = seven_descending(i)
    #val = single_shaped(i)
    #val = single(i)
    #val = one_five_oct(i)
    val = wave_shape(one_five_oct(i))
    
    # print it out
    print "{:.10f}".format(val) + "f, ",
    
    # and draw it out
    if i > -1 and i < 256:
        pixels[i, int(((val + 1) / 2) * 255) + 10] = (0, 0, 0)
        #pixels[i, 10] = (0, 0, 0)
    #
    
img.show()

