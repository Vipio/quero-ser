valor = input("insira um valor redondo: ")

notas_cax = [100, 50, 20, 10]

notas_sac = []

resto = int(valor)

if resto % 10 == 0:
    while resto != 0:
        for i in notas_cax:
                while resto - i >= 0:
                    resto = resto - i 
                    notas_sac.append(i)               
    print("Valor de R$",valor, "emitidos: ", str(notas_sac)[1:-1])
else:
    print("Não é possível sacar o valor, apenas valores redondos")