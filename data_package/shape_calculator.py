import geometry_utils

mode=input("Enter the mode: R for Rectangle/ T for Triangle/ C for Circle")
dict = {
    "C": [geometry_utils.circle_area, geometry_utils.circle_perimeter],
    "R": [geometry_utils.rectangle_area, geometry_utils.rectangle_perimeter],
    "T": geometry_utils.triangle_area
}
if mode=='R':
    l = dict[mode]
    width=int(input('Enter first side'))
    height=int(input('Enter second side'))
    area=l[0]
    peri=l[1]
    print(f"Area: {area(width,height)}, Perimeter: {peri(width,height)}")
elif mode=='T':
    l = dict[mode]
    base = int(input('Enter base'))
    height = int(input('Enter height'))
    area = l
    print(f"Area: {area(base, height)}")
elif mode=="C":
    l=dict[mode]
    radius = int(input('Enter radius'))
    area = l[0]
    peri = l[1]
    print(f"Area: {area(radius)}, Perimeter: {peri(radius)}")
