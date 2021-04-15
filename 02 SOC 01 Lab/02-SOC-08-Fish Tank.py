length = int(input())
width = int(input())
height = int(input())
volume_part = float(input())

water_vol = ((length * width * height) * 0.001) * (1 - (volume_part * 0.01))

print(f'{water_vol:.3f}')

#  V1
#  not_filed = volume_part * 0.01
#  end_vol = tank_vol * (1 - not_filed)
#  print(f'{end_vol:.3f}')
