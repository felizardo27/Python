print('====== EX 033 ======')
# n1= float(input('Digite número 1: '))
# n2= float(input('Digite número 2: '))
# n3= float(input('Digite número 3: '))
# if n1 > n2 and n1 > n3 and n2 > n3:
#     print('O maior número é {} e o menor é {}'.format(n1,n3))
# elif n1 > n2 and n1 > n3 and n3 > n2:
#     print('O maior número é {} e o menor é {}'.format(n1, n2))
# elif n2 > n1 and n2 > n3 and n1 > n3:
#     print('O maior número é {} e o menor é {}'.format(n2, n3))
# elif n2 > n1 and n2 > n3 and n3 > n1:
#     print('O maior número é {} e o menor é {}'.format(n2, n1))
# elif n3 > n2 and n3 > n1 and n1 > n2:
#     print('O maior número é {} e o menor é {}'.format(n3, n2))
# elif n3 > n2 and n3 > n1 and n2 > n1:
#     print('O maior número é {} e o menor é {}'.format(n3, n1))
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a # considerando que o A fosse o menor para eliminar um if
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
