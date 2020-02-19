import matplotlib.pyplot as plt
import urllib.request, json
with urllib.request.urlopen('http://albertocn.sytes.net/2019-2/pi/projeto/geracao_energia.json') as url:
  energia_ano = json.loads(url.read().decode())
  valores = list()
  listaEnergiaDia = list()
  diasGrafico = list()
  mes = '01'
  meses = {'01':'Janeiro', '02':'Fevereiro', '03':'Março', '04':'Abril', '05':'Maio', '06':'Junho', '07':'Julho', '08':'Agosto', '09':'Setembro', '10':'Outubro', '11':'Novembro', '12':'Dezembro'}
  for dia in energia_ano:
    valores.append(list(dia.values()))
  valores.sort()
  for dado in valores:
    if dado[0][5:7] == mes:
      diasGrafico.append('Dia ' + dado[0][8:])
      listaEnergiaDia.append(dado[2])
  plt.plot(diasGrafico, listaEnergiaDia)
  plt.ylabel('Energia Gerada (Kwh)')
  plt.suptitle('Energia Gerada por Dia no Mês de ' + meses[mes])
  plt.show()
