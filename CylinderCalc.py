import math

def cylinder_volume():
    return round(math.pi*radius*radius*height, 2)

def cylinder_surface():
    return round((2*math.pi)*radius*(radius+height) ,2)

choice = input('What you want to calculate?\n1.Cylinder volume\n2.Cylinder surface\n')

if choice in ["1", "2"]:
    pass
else:
    print(f'Select valid number and try again')
    exit(0)

if choice == '1':
    print('You chose volume')
    height = input('Enter h - Height of the cylinder\n')
    radius = input('Enter r - Radius of the base\n')
    height = int(height)
    radius = int(radius)
    print(f'Result is: {cylinder_volume()}')

elif choice == '2':
    print('You chose surface')
    height = input('Enter h - Height of the cylinder\n')
    radius = input('Enter r - Radius of the base\n')
    height = int(height)
    radius = int(radius)
    print(f'Result is: {cylinder_surface()}')
