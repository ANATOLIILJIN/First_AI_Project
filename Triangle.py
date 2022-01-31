name = input('Enter name: ')
lastname = input('Enter last name: ')
age = input('Enter age: ')
print(type(age))anatoli



print('Hello', name, lastname + "! You are", age, 'years old!')
print('Hello ' + name + ' ' + lastname + '! You are ' + str(age) + ' years old!')

side_a = float(input('Enter side A: '))
side_b = float(input('Enter side B: '))
side_c = float(input('Enter side C: '))

half_perimeter = (side_a + side_b + side_c) / 2
triangle_area = (half_perimeter * (half_perimeter - side_a) * (half_perimeter - side_b) *
                 (half_perimeter - side_c)) ** 0.5
print('Area of a triangle is', triangle_area)
