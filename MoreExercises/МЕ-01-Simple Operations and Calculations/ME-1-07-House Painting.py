x_house_height = float(input())
y_house_length = float(input())
h_house_tri_height = float(input())

house_fb_sides = (x_house_height ** 2) * 2 - (1.2 * 2)
house_lr_sides = x_house_height * y_house_length * 2 - (1.5 ** 2) * 2
total_house_sqm = house_fb_sides + house_lr_sides
green_paint = total_house_sqm / 3.4

roof_flats = x_house_height * y_house_length * 2
roof_triangles = (x_house_height * h_house_tri_height / 2) * 2
total_roof_sqm = roof_flats + roof_triangles
red_paint = total_roof_sqm / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
