# A. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint, shuffle

# def rnd_num_not_0_1():


# def gen_x_dict(count):
#     x_dict = {}
    
#     for i in range(count, 1, -1):
#         x_dict[f'x**{i}'] = randint(-10, 10)
    
#     return x_dict

k = 4#randint(0, 10)
# print(gen_x_dict(k))



equation_k_list = []


for degree in range(k, 1, -1):
    equation_k_list.append(f'{randint(-10, 10)} * x**{degree}')
    
equation_k_list.append(f'{randint(-10, 10)} * x')
equation_k_list.append(f'{randint(-10, 10)}')
equation_k_list.append(' = 0')

print(equation_k_list)




for num_elem in range(len(equation_k_list) - 1):
    if equation_k_list[num_elem][0] == '-':
        if equation_k_list[num_elem][1] == '1':
            equation_k_list[num_elem] = equation_k_list[num_elem].replace('1 * ', '')
    else:
        if equation_k_list[num_elem][0] == '1':
            equation_k_list[num_elem] = equation_k_list[num_elem].replace('1 * ', '')
        elif equation_k_list[num_elem][0] == '0':
            equation_k_list[num_elem] = equation_k_list[num_elem].replace('0 * ', '')
    

print(equation_k_list)

equation_k_string = equation_k_list[0]


for i in range(1, len(equation_k_list) - 1):
    if equation_k_list[i][0] == '-':
        equation_k_list[i] = equation_k_list[i].replace('-', ' - ')
        equation_k_string += equation_k_list[i]
    else:
        equation_k_string += ' + '
        equation_k_string += equation_k_list[i]
equation_k_string += equation_k_list[-1]

print(equation_k_list)
print(equation_k_string)
        
        
        
        
        
        
# equation_list = [f'{randint(-10, 10)} * x**{k} + {randint(-10, 10)} * x + {randint(-10, 10)} = 0',
#                  f'{randint(-10, 10)} * x**{k} + {randint(-10, 10)} = 0',
#                  f'{randint(-10, 10)} * x**{k} = 0']


# equation1 = f'{randint(-10, 10)} * x**{k[randint(0, 100)]} + {randint(-10, 10)} * x + {randint(-10, 10)} = 0'
# equation2 = f'{randint(-10, 10)} * x**{k[randint(0, 100)]} + {randint(-10, 10)} = 0'
# equation3 = f'{randint(-10, 10)} * x**{k[randint(0, 100)]} = 0'