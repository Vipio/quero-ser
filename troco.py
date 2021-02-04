valor_pago = input("insira o valor a ser pago: ")
valor_dado = input("insira um valor dado: ")


notas_cax = [100, 50, 20, 10, 5, 1, 0.50, 0.10, 0.05, 0.01]

notas_sac = []

troco = float(valor_dado) - float(valor_pago)

if troco >= 0:
    for i in notas_cax:
        while troco - i >= 0:
            troco = troco - i 
            notas_sac.append(i)               
    print("troco a ser dado" ,round((float(valor_dado) - float(valor_pago)),2), "quantidade de cedulas: ", len(notas_sac))   
else:
    print("Essa operação não é possível, valor negativo (o cliente está devendo)")