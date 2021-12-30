import re
empty = re.compile(r'(\s+)')
statement = '   my name is   Hari  '
mo1 = empty.findall(statement)

y = []
y.append(mo1[0])
y.append(mo1[-1])
print(y)
for i in range(2):

    x = statement.replace(y[i],'')
print(x)