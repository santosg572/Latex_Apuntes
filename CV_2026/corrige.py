file='Agradecimientos_en_articulos_internacionales.tex'

pal1= 'Créditos en: Artículo  internacional, '

filin = open(file,'r')

datos = filin.readlines()

datosT = []

k=1
dd = ''
for ss in datos:
  ss = ss.replace('\n',' ')
  if len(ss) < 2:
    print(k)
    k = k+1
    datosT.append(dd)
    dd = ''
  else:
    dd = dd + ss

print(len(datosT))

print(pal1)

k = 1
for ss in datosT:
  print(pal1)
  print(ss)
  if pal1 in ss:
    print(k)
    k = k+1
  ss = ss.replace(pal1, '')
  print(ss)


