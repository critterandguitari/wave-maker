import math

# we go from -1 to 258 cause we need some bookends for the interpolation
for i in range(-1,258):
    sin1 = math.sin((i / 256.0) * 2. * math.pi)
    sin2 = math.sin((i / 256.0) * 2. * math.pi * 2.)
    sin3 = math.sin((i / 256.0) * 2. * math.pi * 3.)
    sin4 = math.sin((i / 256.0) * 2. * math.pi * 4.)
    val = (sin1 + sin2 + sin3 + sin4) * .25
    print "{:.10f}".format(val) + "f,"
    
    
