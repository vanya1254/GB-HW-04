# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]                    # еще в А расширил

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


def write_to_txt(w_string, name_file):
    with open(f'{name_file}', 'w') as data:                                                                # записывает строку в txt
        data.write(w_string)


k = randint(1, 5)                                                                                          # оставил до 5, чтобы бесполезно большие уравнения не генерились
equation_list_1 = gen_primary_equation_list(k)
equation_list_2 = gen_primary_equation_list(k)
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