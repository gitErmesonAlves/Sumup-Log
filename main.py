Cvalue = float(input("Digite um numero: "))
option = 20

while option != 13:
    print('''
# ------------------------ #
    [ 0 ] Debito
    [ 1 ] 1x no Cartão
    [ 2 ] 2x no Cartão
    [ 3 ] 3x no Cartão
    [ 4 ] 4x no Cartão
    [ 5 ] 5x no Cartão
    [ 6 ] 6x no Cartão
    [ 7 ] 7x no Cartão
    [ 8 ] 8x no Cartão
    [ 9 ] 9x no Cartão
    [ 10 ] 10x no Cartão
    [ 11 ] 11x no Cartão
    [ 12 ] 12X no Cartão
    [ 13 ] Sair do Sistema
# ------------------------ #
    ''''')
    option = int(input("Esperando . . . "))
    if option == 0:
        c = Cvalue
        print("Valor será passado de: {}".format(c))
    elif option == 1:
        c = Cvalue * 0.046
        print("Valor será passado de: {}".format(c))
    elif option == 2:
        c = Cvalue * 0.061
        print("Valor será passado de: {}".format(c))
    elif option == 3:
        c = Cvalue * 0.076
        print("Valor será passado de: {}".format(c))
    elif option == 4:
        c = Cvalue * 0.091
        print("Valor será passado de: {}".format(c))
    elif option == 5:
        c = Cvalue * 0.1
        print("Valor será passado de: {}".format(c))
    elif option == 6:
        c = Cvalue * 0.12
        print("Valor será passado de: {}".format(c))
    elif option == 7:
        c = Cvalue * 0.13
        print("Valor será passado de: {}".format(c))
    elif option == 8:
        c = Cvalue * 0.15
        print("Valor será passado de: {}".format(c))
    elif option == 9:
        c = Cvalue * 0.16
        print("Valor será passado de: {}".format(c))
    elif option == 10:
        c = Cvalue * 0.18
        print("Valor será passado de: {}".format(c))
    elif option == 11:
        c = Cvalue * 0.19
        print("Valor será passado de: {}".format(c))
    elif option == 12:
        c = Cvalue * 0.21
        print("Valor será passado de: {}".format(c))
    elif option == 13:
        print("Finalizando...")
    else:
        print('Opção Invalida !')
