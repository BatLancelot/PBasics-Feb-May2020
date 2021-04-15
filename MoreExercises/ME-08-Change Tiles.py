terrain_side = float(input())
tile_width = float(input())
tile_lenght = float(input())
bench_w = float(input())
bench_L = float(input())

bench_area = bench_w * bench_L
terrain_area = terrain_side * terrain_side
tile_area = tile_width * tile_lenght

tiles = (terrain_area - bench_area) / tile_area
time = tiles * 0.2

print(f'{tiles}')
print(f'{time}')
