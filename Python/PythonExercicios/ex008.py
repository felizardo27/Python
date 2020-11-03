print('====== EX 008 ======')
print('Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros')
# decímetro: 10 decímetros correspondem a 1 metro.
# centímetro: 100 centímetros corresponde a 1 metro.
# milímetro: 1000 milímetros corresponde a 1 metro.
md = float(input('Digite uma distância em metros: '))
km = md / 1000
hm = md / 100
dam = md / 10
dm = md * 10
cm = md * 100
mn = md * 1000
print('A medida de {}m corresponde a \nQuilômetros: {}km\nHectómetros {}hm\nDecâmetros: {}dam\nDecímetros: {:.0f}dm'
      '\nCentímetros: {:.0f}cm\nMilímetros: {:.0f}mn'.format(md, km, hm, dam, dm, cm, mn))
