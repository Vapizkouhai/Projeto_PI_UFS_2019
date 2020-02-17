import urllib.request, json
with urllib.request.urlopen('http://albertocn.sytes.net/2019-2/pi/projeto/geracao_energia.json') as url:
  energia_ano = json.loads(url.read().decode())
  valores = list()
  for dia in energia_ano:
    valores.append(list(dia.values()))
  valores.sort()
  print(valores[0])
