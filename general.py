# -*- coding: utf-8 -*-
import os


# Każda pobrana strona jest osobnym projektem
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project directory ' + directory)
        os.makedirs(directory)


# Tworzenie kolejki i pobieranie danych
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Tworzenie nowego pliku
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Dodawnie danych do istniejących plików
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '/n')


# Usuwanie danych z pliku
def delete_file_contents(path):
    with open(path, 'w'):
        pass


# Odczytywanie danych z pliku i konwersja linii na zadanie
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Tworzenie iteracji, każdy element będzie w nowej linii
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)
