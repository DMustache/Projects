import subprocess

with open('Python\\file.txt', mode='r') as f:
    text = f.read() # Чиатем файл https://tproger.ru/articles/files-in-python/
abcl = [chr(i) for i in range(ord('A'), ord('Z') + 1)] # Создаем алфавит
# chr - https://pythonz.net/references/named/chr/
# ord - https://pythonz.net/references/named/ord/
abc = ''.join(abcl) # так как работать со списком сложнее, то перенесем из списка в строку наш алфавит
del abcl # удалим алфавит

for i in range(len(abc)): # Основной цикл
    string = abc[0:len(abc) - i] # создаем строку, которую будем искать в файле
    if string in text: # если строка в файле
        print(string) #  показываем ее
        subprocess.check_call(f'echo {string}|clip', shell=True)
        break # Заканчиваем выполнение кода, т.к. эта строка самая большая в файле
    else:
        continue # так красивиее выглядит код)))