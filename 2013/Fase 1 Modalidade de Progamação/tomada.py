'''A Olimpíada Internacional de Informática (IOI, no original em inglês) é a mais prestigiada competição de
programação para alunos de ensino médio; seus aproximadamente 300 competidores se reúnem em um país
diferente todo ano para os dois dias de prova da competição. Naturalmente, os competidores usamo o tempo
livre para acessar a Internet, programar e jogar em seus notebooks, mas eles se depararam com um problema:
o saguão do hotel só tem uma tomada.
Felizmente, os quatro competidores da equipe brasileira da IOI trouxeram cada um uma régua de tomadas,
permitindo assim ligar vários notebooks em uma tomada só; eles também podem ligar uma régua em outra
para aumentar ainda mais o número de tomadas disponíveis. No entanto, como as réguas têm muitas
tomadas, eles pediram para você escrever um programa que, dado o número de tomadas em cada régua,
determina quantas tomadas podem ser disponibilizadas no saguão do hotel.'''


#Forma mais simples

'''
reguas= input("Digite seus números").split()
somaDeTomadas = 1 #começa com 1 pois sempre vai  ter uma tomada no hotel mesmo que nenhum deles traga uma regua de tomada
if len(reguas) >= 2 and len(reguas) <= 6:
    for i in reguas:
        somaDeTomadas += int(i) - 1
print(somaDeTomadas)

'''

#Tentativa mais elaborada 
x = input().split()
reguas = []
for i in x:
    reguas.append(int(i))
if len(reguas) >= 2 and len(reguas) <= 6:
    somaDeTomadas = sum(reguas) - (len(reguas)-1)
else:
    print("Suas entradas precisam de acordo com a lógica")

print(somaDeTomadas)