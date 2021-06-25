# EXEMPLO 2
## Faça um algoritmo que mostre todos os números primos de 1 a 200.

## Loop para os números de 1 a 100
for cont in range(2,200):
    ## Número 2 já é primo, então imprime
    if cont == 2:
        print(cont)
    else:
        ##Loop para verificar os divisores
        for cont2 in range(2,cont):
            ## Se o número verificado já for divisivel por outros
            ## sem ser 1 e ele mesmo, já paro o loop (já sei que não é primo)
            if cont % cont2 == 0:
                break
            ## Se ele fez a verificação de todos os numeros e nenhum é divisivel
            ## Ele é primo, ai imprimo!! :)
            if cont2+1 == cont:
                print(cont)