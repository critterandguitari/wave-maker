import math

# we go from -1 to 258 cause we need some bookends for the interpolation
for i in range(-1,258):
    sin1 = math.sin((i / 256.0) * 2. * math.pi)
    val = sin1
    print "{:.10f}".format(val) + "f,"
    
    
