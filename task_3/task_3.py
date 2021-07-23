import os
import pathlib
from pathlib import Path


folder_path = os.getcwd()
folder_path_1 = Path(f'{folder_path}/folder')


def sorting_txt_files(folder):
    list_txt_files = [file for file in os.listdir(folder) if file.endswith('.txt')]
    return list_txt_files


def creating_dict(list_n):
    dict_files = {}
    for f in list_n:
        with open(folder_path_1/f, encoding='utf-8') as file:
            file_read = file.read()
            with open(folder_path_1/f, 'r', encoding='utf-8') as file:
                list_properties = []
                list_properties.append(len(file.readlines()))
                list_properties.append(file_read)
                dict_files[pathlib.Path(file.name).name] = list_properties
    sorted_dict = dict(sorted((dict_files.items()), key=lambda x: x[1][0]))
    return sorted_dict


def creating_common_file(dict_n):
    with open('common.txt', 'a', encoding='utf-8') as f:
        for file in dict_n:
            f.write(file + '\n')
            f.write(str(dict_n[file][0]) + '\n')
            f.write(str(dict_n[file][1]) + '\n')
            f.write('\n')
    return


creating_common_file(creating_dict(sorting_txt_files(folder_path_1)))

