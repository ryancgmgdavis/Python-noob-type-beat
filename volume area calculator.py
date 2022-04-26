import math
print("\n\n\n")

#da numbahs
var1 = float(input("type a number beybee "))

#da math bits

#area
a_squ = var1 * 2
a_cir = math.pi * var1 ** 2
a_pent = (1 / 4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * var1 ** 2
a_tri = (math.sqrt(3) / 4) * var1 ** 2
#volume
vol_cube = var1 ** 3
vol_sph = (4 / 3) * math.pi * (var1 ** 3)
vol_dod = ((15 + 7 * math.sqrt(5)) / 4) * var1 ** 3
vol_icos = (5 * (3 + math.sqrt(5)) / 12) * var1 ** 3

#display

#square
print(f"The area of a square with a side length of {var1} is: {a_squ:.2f}")
print(f"The volume of a cube with a edge length of {var1} is: {vol_cube:.2f}\n")
#circle
print(f"The area of a circle with a radius of {var1} is: {a_cir:.2f}")
print(f"The volume of a sphere with a radius of {var1} is: {vol_sph:.2f}\n")
#pentagon
print(f"The area of a pentagon with a side length of {var1} is: {a_pent:.2f}")
print(f"The volume of a dodecahedron with an edge length of {var1} is: {vol_dod:.2f}\n")
#triangle
print(f"The area of a triangle with a side length of {var1} is: {a_tri:.2f}")
print(f"The volume of a icosahedron with an edge length of {var1} is: {vol_icos:.2f}\n")
print("\n\n\n")