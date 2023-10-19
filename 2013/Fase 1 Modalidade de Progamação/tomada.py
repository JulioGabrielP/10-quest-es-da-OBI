reguas= input("Digite seus números").split()
somaDeTomadas = 1 #começa com 1 pois sempre vai  ter uma tomada no hotel mesmo que nenhum deles traga uma regua de tomada
if len(reguas) >= 2 and len(reguas) <= 6:
    for i in reguas:
        somaDeTomadas += int(i) - 1
print(somaDeTomadas)
