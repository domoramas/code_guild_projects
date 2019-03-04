#unit_converter.py
to_meters = {'ft': 0.3048, 'mi': 1609.34, 'm':1, 'km':1000, 'yd':0.9144, 'in':0.0254}
in_num =int(input(f'What is the distance ?>'))

in_unit =input(f'What are the input units?>')
while in_unit not in to_meters.keys():
    print(f'Invalid input')
    in_unit =input(f'What are the input units?>')

out_unit =input(f'What are the output units?>')
while out_unit not in to_meters.keys():
    print(f'Invalid input')
    out_unit =input(f'What are the output units?>')

print(f"{in_num} {in_unit} is {round(in_num * to_meters[in_unit]/to_meters[out_unit],2)} {out_unit}")
