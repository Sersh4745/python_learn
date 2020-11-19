"""
    Дан файл с текстом (text.txt).
    Создать новый файл (edited_text.txt), каждая строка которого получается из
    соответствующей строки исходного файла с обратным порядком слов, причем
    первое слово с заглавной буквы, а все остальные со строчной.

    Например 1 файл содержит:
    Hello world
    How are you

    Тогда второй файл будет содержать:
    World hello
    You are how
"""
data = None
with open('C:/Users/Sersh/python_basic/python_basic/hw7/text.txt') as f:
    data = f.readlines()

with open('Diachenko.hw7/edited_text.txt','w') as file:
    #ed_text = data.split()
    ed_text = data
    ed_text = ed_text[::-1]
    for i in ed_text:
        i = i.lower()
        i = i.split(' ')[::-1]
        x =[]
        for s in i:
            if '.\n' in s:
                s = s.capitalize()
                x.append(s.replace('.\n',''))
            else:
                x.append(s)
        x.append('.\n')
        file.write(' '.join(x))
    

        
