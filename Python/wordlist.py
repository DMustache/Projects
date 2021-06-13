import docx
doc = docx.Document(r'C:\Users\DVUsa\Downloads\11_База_СПИСОК произведений для чтения_РАССЫЛКА.docx')

wordlist = []
with open(r'Python\www.txt', 'w+') as fin:
    with open(r'Python\www.txt', 'w') as fout:
        delete = ['Гоголь Н.', 'o']
        for line in fin:
            if delete in line:
                print(line.index(delete))
            else:
                fout.write(f'{line}\n')
