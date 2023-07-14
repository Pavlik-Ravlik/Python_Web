spisok = ['a', 'b', 'c']

spisok_1 = ['d', 'e', 'f']


for i in spisok_1:
    if spisok_1 not in spisok:
        spisok.append(i)



print(spisok)