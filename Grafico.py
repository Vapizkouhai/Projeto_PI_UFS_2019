import matplotlib.pyplot as plt, urllib.request, json
with urllib.request.urlopen('http://albertocn.sytes.net/2019-2/pi/projeto/geracao_energia.json') as url:
  energia_ano = json.loads(url.read().decode())
  valores = list()
  listaEnergiaDia = list()
  diasGraficoLinhas = list()
  mesGraficoLinhas = '12'
  meses = {'01':'Janeiro', '02':'Fevereiro', '03':'Março', '04':'Abril', '05':'Maio', '06':'Junho', '07':'Julho', '08':'Agosto', '09':'Setembro', '10':'Outubro', '11':'Novembro', '12':'Dezembro'}  
  grafico = plt.figure()
  plt.style.use('seaborn')
  for dia in energia_ano:
    valores.append(list(dia.values()))
  valores.sort()
  axis1 = grafico.add_subplot(2, 2, 1)
  if mesGraficoLinhas in list(meses.keys()):
    for dado in valores:
      if dado[0][5:7] == mesGraficoLinhas:
        diasGraficoLinhas.append(dado[0][8:])
        listaEnergiaDia.append(dado[2])
    axis1.plot(diasGraficoLinhas, listaEnergiaDia)
    axis1.set_ylabel('Energia Gerada (Kwh)')
    axis1.set_xlabel('Dias de Produção')
    axis1.set_title('Energia Gerada por Dia no Mês de ' + meses[mesGraficoLinhas])
  else:   
    axis1.set_title('Mês ' + mesGraficoLinhas + ' não existente')
  axis2 = grafico.add_subplot(2, 2, 2)
  
  axis3 = grafico.add_subplot(2, 1, 2)
  boxplotVerão = list()
  boxplotOutono = list()
  boxplotInverno = list()
  boxplotPrimavera = list()
  for dado in valores:
    if dado[0][5:7] in ['12', '01', '02']:
      boxplotVerão.append(dado[2])
    elif dado[0][5:7] in ['03', '04', '05']:
      boxplotOutono.append(dado[2])
    elif dado[0][5:7] in ['06', '07', '08']:
      boxplotInverno.append(dado[2])
    elif dado[0][5:7] in ['09', '10', '11']:
      boxplotPrimavera.append(dado[2])
  axis3.boxplot([boxplotVerão, boxplotOutono, boxplotInverno, boxplotPrimavera])
  axis3.set_xticklabels(['Verão', 'Outono', 'Inverno', 'Primavera'])
  axis3.set_ylabel('Energia Gerada (Kwh)')
  axis3.set_xlabel('Estações Meteorológicas')
  axis3.set_title('Energia Gerada em Cada Estação Meteorológica')
  grafico.subplots_adjust(left=.07, bottom=.07, right=.95, top=.95, wspace=.15, hspace=.22)
  plt.show()
