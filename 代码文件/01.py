values = [k.strip() for k in open('userdict.txt', encoding='utf8').readlines() if k.strip() != '']
for i in values:
   print(i)