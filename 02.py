# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]                    # еще в А расширил

from random import randint


def gen_primary_equation_list(max_degree):
    primary_equation_list = []
    
    for degree in range(max_degree, 1, -1):
        primary_equation_list.append(f'{randint(-10, 10)} * x**{degree}')
        
    primary_equation_list.append(f'{randint(-10, 10)} * x')
    primary_equation_list.append(f'{randint(-10, 10)}')
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


def write_to_txt(w_string, name_file):
    with open(f'{name_file}', 'w') as data:                                                                # записывает строку в txt
        data.write(w_string)


def read_txt(name_file):
    with open(f'{name_file}', 'r') as data:                                                                # считывает строку в txt
        return data.read()


def get_dict_from_list(equation):
    equation_dict = {'default':'',}
    
    for item in range(len(equation) - 1):
        if item == 0 and equation[item].find('x') == -1:
            equation_dict.setdefault(f'{equation[item + 2]}', f'{equation[item]}')
        elif equation[item].find('x') != -1 and equation[item].find('-') != -1:
            equation_dict.setdefault(f'{equation[item][1:]}', f'-1')
        elif equation[item].find('x') != -1 and equation[item].find('-') == -1 and equation[item - 1] != '-':
            equation_dict.setdefault(f'{equation[item]}', f'1')
        elif equation[item].find('x') != -1 and equation[item].find('-') == -1 and equation[item - 1] == '-':
            equation_dict.setdefault(f'{equation[item]}', f'-1')
        elif equation[item].find('x') != -1 and equation[item].find('-') == -1 and equation[item - 1] == '+':            # я не смог лучше хотел словарями сложить
            equation_dict.setdefault(f'{equation[item]}', f'1')
        elif equation[item].isdigit() and equation[item + 2].find('x') != -1 and equation[item - 1] == '-':
            equation_dict.setdefault(f'{equation[item + 2]}', f'-{equation[item]}')
        elif equation[item].isdigit() and equation[item + 2].find('x') != -1 and equation[item - 1] == '+':
            equation_dict.setdefault(f'{equation[item + 2]}', f'{equation[item]}')
        elif equation[item].isdigit() and equation[item + 2].find('x') == -1 and equation[item - 1] == '-':
            equation_dict.setdefault(f'{equation[-2]}', f'-{equation[item]}')
        elif equation[item].isdigit() and equation[item + 2].find('x') == -1 and equation[item - 1] == '+':
            equation_dict.setdefault(f'{equation[-2]}', f'{equation[item]}')
    del equation_dict['default']
    
    return equation_dict


def get_dict_sum_equations(equation_1, equation_2):
    equations_list = [equation_1, equation_2]
    sum_equations = {}
    
    for dict in equations_list:
        for k in dict.keys():
            sum_equations[k] = int(sum_equations.get(k,0)) + int(dict[k])

    return(sum_equations)


def get_string_from_dict_equations(equations_dict):
    equations_string = ''
    
    for k, v in sorted(equations_dict.items(), reverse=True):
        if k != '=':
            if v == -1:
                equations_string += f"- {k} "
            elif v == 0:
                equations_string += ""
            elif v == 1:
                equations_string += f"+ {k} "                                                                # собирает правильную строку суммы из словаря
            else:
                if v > 1:
                    equations_string += f"+ {v} * {k} "
                elif v < 1:
                    equations_string += f"- {abs(v)} * {k} "

        if k == '=':
                if v > 0:
                    equations_string += f"+ {v} = 0"
                elif v == 0:
                    equations_string += "= 0"
                elif v < 0:
                    equations_string += f"- {abs(v)} = 0"
    
    if equations_string[0] == '-':
        equations_string = equations_string.replace(' ','', 1)
    elif equations_string[0] == '+':
        equations_string = equations_string.replace('+ ','', 1)

    return equations_string


k_1 = randint(1, 5)                                                                                          # оставил до 5, чтобы бесполезно большие уравнения не генерились
k_2 = randint(1, 5)
equation_list_1 = gen_primary_equation_list(k_1)
equation_list_2 = gen_primary_equation_list(k_2)
# print(equation_list_1, equation_list_2)

formatting_equation_list(equation_list_1)
formatting_equation_list(equation_list_2)
# print(equation_list_1, equation_list_2)

equation_rnd_string_1 = get_rnd_string_equation(equation_list_1)
equation_rnd_string_2 = get_rnd_string_equation(equation_list_2)
print(equation_rnd_string_1)
print(equation_rnd_string_2)

write_to_txt(equation_rnd_string_1, 'equation_1.txt')
write_to_txt(equation_rnd_string_2, 'equation_2.txt')


equation_split_string_1 = read_txt('equation_1.txt').split()
equation_split_string_2 = read_txt('equation_2.txt').split()
# print(equation_split_string_1)
# print(equation_split_string_2)

equation_dict_1 = get_dict_from_list(equation_split_string_1)
equation_dict_2 = get_dict_from_list(equation_split_string_2)
# print(equation_dict_1)
# print(equation_dict_2)

sum_equations_dict = get_dict_sum_equations(equation_dict_1, equation_dict_2)
# print(sum_equations_dict)

sum_equations_string = get_string_from_dict_equations(sum_equations_dict)
print(sum_equations_string)

write_to_txt(sum_equations_string, 'equations_sum.txt')