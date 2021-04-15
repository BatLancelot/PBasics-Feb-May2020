size = float(input())
in_metric = input().lower()
out_metric = input().lower()

if in_metric == 'yd':
    if out_metric == 'km':
        size = size * 0.0009144
        print(f'{size}')
    elif out_metric == 'm':
        size = size * 0.9144
        print(f'{size}')
    elif out_metric == 'mm':
        size = size * 914.4
        print(f'{size}')
    elif out_metric == 'cm':
        size = size * 91.44
        print(f'{size}')
    elif out_metric == 'mi':
        size = size * 0.0005681818
        print(f'{size}')
    elif out_metric == 'in':
        size = size * 36
        print(f'{size}')
    elif out_metric == 'ft':
        size = size * 3
        print(f'{size}')
    else:
        print(f'{size}')

if in_metric == 'ft':
    if out_metric == 'km':
        size = size * 0.0003048
        print(f'{size}')
    elif out_metric == 'm':
        size = size * 0.3048
        print(f'{size}')
    elif out_metric == 'mm':
        size = size * 304.8
        print(f'{size}')
    elif out_metric == 'cm':
        size = size * 30.48
        print(f'{size}')
    elif out_metric == 'mi':
        size = size * 0.0001893939
        print(f'{size}')
    elif out_metric == 'in':
        size = size * 12
        print(f'{size}')
    elif out_metric == 'yd':
        size = size * 0.3333333333
        print(f'{size}')
    else:
        print(f'{size}')

if in_metric == 'in':
    if out_metric == 'km':
        size = size * 0.0000254
        print(f'{size}')
    elif out_metric == 'm':
        size = size * 0.0254
        print(f'{size}')
    elif out_metric == 'mm':
        size = size * 25.4
        print(f'{size}')
    elif out_metric == 'cm':
        size = size * 2.54
        print(f'{size}')
    elif out_metric == 'mi':
        size = size * 0.00001578283
        print(f'{size}')
    elif out_metric == 'ft':
        size = size * 0.0833333333
        print(f'{size}')
    elif out_metric == 'yd':
        size = size * 0.0277777778
        print(f'{size}')
    else:
        print(f'{size}')

if in_metric == 'mi':
    if out_metric == 'km':
        size = size * 1.609344
        print(f'{size}')
    elif out_metric == 'm':
        size = size * 1609.344
        print(f'{size}')
    elif out_metric == 'mm':
        size = size * 1609344
        print(f'{size}')
    elif out_metric == 'cm':
        size = size * 160934.4
        print(f'{size}')
    elif out_metric == 'in':
        size = size * 63360
        print(f'{size}')
    elif out_metric == 'ft':
        size = size * 5280
        print(f'{size}')
    elif out_metric == 'yd':
        size = size * 1760
        print(f'{size}')
    else:
        print(f'{size}')

if in_metric == 'cm':
    if out_metric == 'km':
        size = size * 0.00001
        print(f'{size}')
    elif out_metric == 'm':
        size = size * 0.01
        print(f'{size}')
    elif out_metric == 'mm':
        size = size / 0.1
        print(f'{size}')
    elif out_metric == 'mi':
        size = size * (0.000621371192 * 0.01)
        print(f'{size}')
    elif out_metric == 'in':
        size = size * (39.3700787 * 0.01)
        print(f'{size}')
    elif out_metric == 'ft':
        size = size * (3.2808399 * 0.01)
        print(f'{size}')
    elif out_metric == 'yd':
        size = size * (1.0936133 * 0.01)
        print(f'{size}')
    else:
        print(f'{size}')

if in_metric == 'mm':
    if out_metric == 'km':
        size = size * 0.000001
        print(f'{size}')
    elif out_metric == 'm':
        size = size * 0.001
        print(f'{size}')
    elif out_metric == 'cm':
        size = size * 0.1
        print(f'{size}')
    elif out_metric == 'mi':
        size = size * (0.000621371192 * 0.001)
        print(f'{size}')
    elif out_metric == 'in':
        size = size * (39.3700787 * 0.001)
        print(f'{size}')
    elif out_metric == 'ft':
        size = size * (3.2808399 * 0.001)
        print(f'{size}')
    elif out_metric == 'yd':
        size = size * (1.0936133 * 0.001)
        print(f'{size}')
    else:
        print(f'{size}')

if in_metric == 'm':
    if out_metric == 'km':
        size = size * 0.001
        print(f'{size}')
    elif out_metric == 'mm':
        size = size * 1000
        print(f'{size}')
    elif out_metric == 'cm':
        size = size * 100
        print(f'{size}')
    elif out_metric == 'mi':
        size = size * 0.000621371192
        print(f'{size}')
    elif out_metric == 'in':
        size = size * 39.3700787
        print(f'{size}')
    elif out_metric == 'ft':
        size = size * 3.2808399
        print(f'{size}')
    elif out_metric == 'yd':
        size = size * 1.0936133
        print(f'{size}')
    else:
        print(f'{size}')

if in_metric == 'km':
    if out_metric == 'm':
        size = size * 1000
        print(f'{size}')
    elif out_metric == 'mm':
        size = size * 1000000
        print(f'{size}')
    elif out_metric == 'cm':
        size = size * 100000
        print(f'{size}')
    elif out_metric == 'mi':
        size = size * 0.6213711922
        print(f'{size}')
    elif out_metric == 'in':
        size = size * 39370.078740157
        print(f'{size}')
    elif out_metric == 'ft':
        size = size * 3280.8398950131
        print(f'{size}')
    elif out_metric == 'yd':
        size = size * 1093.6132983377
        print(f'{size}')
    else:
        print(f'{size}')
