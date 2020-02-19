import matplotlib.pyplot as plt
import urllib.request, json
with urllib.request.urlopen('http://albertocn.sytes.net/2019-2/pi/projeto/geracao_energia.json') as url:
  energia_ano = json.loads(url.read().decode())
  valores = list()
  listaEnergiaDia = list()
  diasGrafico = list()
  for dia in energia_ano:
    valores.append(list(dia.values()))
  valores.sort()
  for dado in valores:
    if dado[0][5:7] == '01':
      diasGrafico.append('Dia ' + dado[0][8:])
      listaEnergiaDia.append(dado[2])
  print(listaEnergiaDia)
  print(diasGrafico)
  plt.plot(diasGrafico, listaEnergiaDia)
  plt.show()
