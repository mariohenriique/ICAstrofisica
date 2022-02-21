nome = []
RA = []
Dec = []
Glon = []
Glat = []
pmra = []
pmde = []
plx = []
dist = []
logt = []
ref = []
arquivo = open('lista11','r')
arquivo.close

for linha in arquivo:
  nome.append(linha.split()[0])
  RA.append(linha.split()[1])
  Dec.append(linha.split()[2])
  Glon.append(linha.split()[3])
  Glat.append(linha.split()[4])
  pmra.append(linha.split()[5])
  pmde.append(linha.split()[6])
  plx.append(linha.split()[7])
  dist.append(linha.split()[8])
  logt.append(linha.split()[9])
  ref.append(linha.split()[10])

nome.pop(0)
RA.pop(0)
Dec.pop(0)
Glon.pop(0)
Glat.pop(0)
pmra.pop(0)
pmde.pop(0)
plx.pop(0)
dist.pop(0)
logt.pop(0)
ref.pop(0)
nome

import os

for i in nome:
#  os.makedirs(i + '/Fits')
#  os.makedirs(i + '/Graficos')
#  os.makedirs(i + '/CSV')
  posi = nome.index(i)
  with open(i + '/coordenadas_' + i + '.txt','w') as arquivo:
    arquivo.write('RA  ' + RA[posi] + '\n' + 'Dec ' + Dec[posi])
