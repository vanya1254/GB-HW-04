# A. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


def gen_primary_equation_list(max_degree):
    primary_equation_list = []
    
    for degree in range(max_degree, 1, -1):
        primary_equation_list.append(f'{randint(-100, 100)} * x**{degree}')
        
    primary_equation_list.append(f'{randint(-100, 100)} * x')
    primary_equation_list.append(f'{randint(-100, 100)}')
    primary_equation_list.append(' = 0')
    
    return primary_equation_list


def formatting_equation_list(equation_list):
    for num_elem in range(len(equation_list) - 1):
        if equation_list[num_elem][0] == '-':
            equation_list[num_elem] = equation_list[num_elem].replace('-', ' - ')
            
            if equation_list[num_elem][3] == '1' and equation_list[num_elem][-1:3:-1].find('1') == -1:
                equation_list[num_elem] = equation_list[num_elem].replace('1 * ', '')
        else:
            if equation_list[num_elem][0] == '1' and equation_list[num_elem][-1:0:-1].find('1') == -1:
                equation_list[num_elem] = equation_list[num_elem].replace('1 * ', '')                      # избавляется от 1 0 -1 перед х и правит отступы у "-"
            elif equation_list[num_elem][0] == '0':
                equation_list[num_elem] = equation_list[num_elem].replace('0 * ', '')


def get_rnd_string_equation(equation_list, rnd_choice = randint(1, 3)):
    equation_string = equation_list[0].replace(' - ', '-')
    
    if rnd_choice == 1:
        for i in range(1, len(equation_list) - 1):
            if equation_list[i].find('-') != -1:
                equation_string += equation_list[i]                                                        # собирает строку полного многочлена
            else:
                equation_string += ' + '
                equation_string += equation_list[i]
        equation_string += equation_list[-1]
    elif rnd_choice == 2:
        if equation_list[-2].find('-') != -1:
            equation_string += equation_list[-2]                                                           # собирает строку среднего по наполненности многочлена
        else:
            equation_string += ' + '
            equation_string += equation_list[-2]
        equation_string += equation_list[-1]
    elif rnd_choice == 3:
        equation_string += equation_list[-1]                                                               # собирает строку минимальную по наполненности многочлена

    return equation_string


k = randint(1, 5)                                                                                          # оставил до 5, чтобы бесполезно большие уравнения не генерились
equation_list = gen_primary_equation_list(k)
# print(equation_list)

formatting_equation_list(equation_list)
# print(equation_list)

equation_rnd_string = get_rnd_string_equation(equation_list)
print(equation_rnd_string)





















# def rnd_num_not_0_1():


# def gen_x_dict(count):
#     x_dict = {}
    
#     for i in range(count, 1, -1):
#         x_dict[f'x**{i}'] = randint(-10, 10)
    
#     return x_dict

# k = 4#randint(0, 10)
# print(gen_x_dict(k))



# k = 4#randint(0, 10)

# equation_k_list = []


# for degree in range(k, 1, -1):
#     equation_k_list.append(f'{randint(-10, 10)} * x**{degree}')
    
# equation_k_list.append(f'{randint(-10, 10)} * x')
# equation_k_list.append(f'{randint(-10, 10)}')
# equation_k_list.append(' = 0')

# print(equation_k_list)




# for num_elem in range(len(equation_k_list) - 1):
#     if equation_k_list[num_elem][0] == '-':
#         equation_k_list[num_elem] = equation_k_list[num_elem].replace('-', ' - ')
        
#         if equation_k_list[num_elem][3] == '1':
#             equation_k_list[num_elem] = equation_k_list[num_elem].replace('1 * ', '')
#     else:
#         if equation_k_list[num_elem][0] == '1':
#             equation_k_list[num_elem] = equation_k_list[num_elem].replace('1 * ', '')             # избавляется от 1 0 -1 перед х и правит отступы у "-"
#         elif equation_k_list[num_elem][0] == '0':
#             equation_k_list[num_elem] = equation_k_list[num_elem].replace('0 * ', '')
    

# print(equation_k_list)






# # print(choice(equation_k_list[:-1]))


# equation_k_string = equation_k_list[0].replace(' - ', '-')                                        # прилипляет - к первому члену если есть и присваивает его началу строки

# # index_last_elem = -2
# # index_equal = -1


# # for i in range(1, len(equation_k_list) - 1):
# #     if equation_k_list[i].find('-') != -1:
# #         equation_k_string += equation_k_list[i]                                                 # собирает строку полного многочлена
# #     else:
# #         equation_k_string += ' + '
# #         equation_k_string += equation_k_list[i]
# # equation_k_string += equation_k_list[-1]




# # if equation_k_list[-2].find('-') != -1:
# #     equation_k_string += equation_k_list[-2]                                                      # собирает строку среднего по наполненности многочлена
# # else:
# #     equation_k_string += ' + '
# #     equation_k_string += equation_k_list[-2]
# # equation_k_string += equation_k_list[-1]




# equation_k_string += equation_k_list[-1]                                                      # собирает строку минимальную по наполненности многочлена





# print(equation_k_list)
# print(equation_k_string)
        
        
        
        
        
        
# equation_list = [f'{randint(-10, 10)} * x**{k} + {randint(-10, 10)} * x + {randint(-10, 10)} = 0',
#                  f'{randint(-10, 10)} * x**{k} + {randint(-10, 10)} = 0',
#                  f'{randint(-10, 10)} * x**{k} = 0']


# equation1 = f'{randint(-10, 10)} * x**{k[randint(0, 100)]} + {randint(-10, 10)} * x + {randint(-10, 10)} = 0'
# equation2 = f'{randint(-10, 10)} * x**{k[randint(0, 100)]} + {randint(-10, 10)} = 0'
# equation3 = f'{randint(-10, 10)} * x**{k[randint(0, 100)]} = 0'