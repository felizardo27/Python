## 'curso em video python' - cadeia de caracteres (string)
# frase = 'Curso em Vídeo Python'
# |C|U|R|S|O| |E|M| |V|I |D |E |O |  |P |Y |T |H |O |N |
# |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|
frase = 'Curso em Video Python'
# print(frase[9])
# print(frase[9:14]) # o ultimo valor não entra
# print(frase[9:21:2]) # 0:0:2 - pula de 2 em dois
# print(frase[:5]) # Começa do inicio
# print(frase[15:]) # Vai até o final
# print(frase[9::3]) # Começa do 9, vai ate o final, e pula de 3 em 3
# Analise
# print(len(frase))  # Mostra o tamanho da string
# print(frase.count('o'))  # Conta quantas letras existe na string
# print(frase.count('o', 0, 13))  # Conta quantas letras, considerando do 0 ate o 13
# print(frase.find('deo'))  # Acha uma frase na string, mostrando onde começa a contar
# print(frase.find('Android'))  # retorna -1 quando não existe essa string
# print(frase.replace('Python', 'Android')) #procura determinada palavra na string e substitui por outra
# print(frase.upper()) # transforma a frase toda em maiuscula
# print(frase.lower()) # transforma tudo em minusculo
# print(frase.capitalize()) # Coloca a primeira letra em maiusculo e deixa o resto em minusculo
# print(frase.title()) # Transforma cada palavra seprada em espaços em maiusculo
# frase2 = '   Aprenda Python   '
# print(frase2.strip()) # Remove os espaços não usados, no começo da string e no final
# print(frase2.rstrip()) # Remove somente os espaços direitos
# print(frase2.lstrip()) # Remove somente os espaços esquerdos
# Divisao
# print(frase.split()) # faz uma divisao na string considerando os espaços, dividindo a string
