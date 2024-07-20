import sys

image_width = 256
image_height = 256

print("P3\n" , image_width , ' ' , image_height , "\n255\n")

for j in range(image_height):
    print("\rScanline remaining: " , image_height - j, "\n", file=sys.stderr)
    for i in range(image_width): 
        r = i / (image_width - 1)
        g = j / (image_height - 1)
        b = 0.0

        ir = int(255.999 * r)
        ig = int(255.999 * g)
        ib = int(255.999 * b)

        print(ir , ' ' , ig , ' ' , ib , '\n')

print("\rDone:" , file=sys.stderr)
