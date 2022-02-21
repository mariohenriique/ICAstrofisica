arquivo = open('lista11', 'r')
with open('parametro_para_rodar_programa.txt','w') as arquivopronto:
  for e in range(15): 
    semlinha = arquivo.readline()
    semlinhas = ','.join(semlinha.split())
    arquivopronto.write(semlinhas + '\n')
arquivo.close()
