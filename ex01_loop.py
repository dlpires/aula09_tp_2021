# EXEMPLO 1
## Faça um algoritmo que peça ao usuário digitar um número natural maior que 1 e mostre os números de 1
## até o número que ele digitou.

#Pedir ao usuário pra digitar número lindo e muito simpático!!

numero = input("Digite um número:")

## Se o que o usuario digitou não é um numero, informe a ele o erro
if not numero.isdigit():
    print("Erro: Isto não é um número ou é um numero negativo!")
## Caso o primeiro Se passe, verifique se o numero ele é menor ou igual a 1
elif int(numero) <= 1:
    print("Erro: Digite um numero maior do que 1!")
##Se nenhum dos dois casos ocorreu, imprima os numeros
else:
    ## Transforma o numero digitado, que esta em texto, para numero
    numero = int(numero)

    print("######### PRINT COM O PARA (FOR) ##########")

    ## ESTRUTURA PARA em PYTHON (Inicio, Fim, Passo -> 1 em 1, 2 em 2 ....)
    for contador in range(1, numero+1,1):
        print("Este é o numero", contador)

    ## ESTRUTURA ENQUANTO (WHILE)
    contador = 1
    
    print("######### PRINT COM O ENQUANTO (WHILE) ##########")
    ## ENQUANTO O CONTADOR FOR MENOR OU IGUAL AO VALOR DIGITADO, FAÇA ISSO
    while contador <= numero:
        #IMPRIMA O NUMERO
        print("Este é o numero", contador)
        #SOME MAIS UM AO CONTADOR
        contador = contador + 1

    
    print("######### PRINT COM O REPITA ATÉ (GAMBIARRA / NÃO EXISTE EM PYTHON) ##########")
    ## INICIO DO CONTADOR
    contador = 1

    ## ENQUANTO O CONTADOR FOR MENOR OU IGUAL AO VALOR DIGITADO, FAÇA ISSO
    while True:
        #IMPRIMA O NUMERO
        print("Este é o numero", contador)
        #SOME MAIS UM AO CONTADOR
        contador = contador + 1
        #VALIDAÇÃO VERIFICANDO SE O CONTADOR JÁ CHEGOU AO NUMERO (SE / SENÃO)
        if contador > numero:
            break

    


