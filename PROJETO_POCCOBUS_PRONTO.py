def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


print('-*-'*15)
print('  Bem vindo a venda de passagem POCCOBUS!  ')
print('-*-'*15)
print()


def menu_passagem():
    print('--'*15)
    print('       ----M E N U----')
    print('''    [ 1 ] Comprar passagem
    [ 2 ] Ver Poltronas
    [ 3 ] Gerar Relatório
    [ 4 ] Finalizar Vendas''')
    print('--' * 15)


janela_direita = [0] * 7
corredor_direita = [0] * 7
corredor_esquerda = [0] * 7
janela_esquerda = [0] * 7
total_vendido = 0


def poltronas():
    print()
    print('--' * 21)
    print('Janela Direita:    ', janela_direita)
    print('Corredor Direita:  ', corredor_direita)
    print('Corredor Esquerda: ', corredor_esquerda)
    print('Janela Esquerda:   ', janela_esquerda)
    print('--' * 21)
    print('LEGENDA')
    print('Lugares vagos [0] - Lugares ocupados [x]')
    print()


def vender_passagem():
    global total_vendido
    while (total_vendido <= 28):
        print()
        opcao = str(input('Digite opcao Janela [J] ou Corredor [C]?: ')).strip().upper()[0]
        if opcao == 'J':
            opcao2 = str(input('Janela direita [D] ou esquerda [E]: ')).strip().upper()[0]
            if opcao2 == 'D':
                if janela_direita == ['x', 'x', 'x', 'x', 'x', 'x', 'x']:
                    print('Todos os lugares estão ocupados!')
                    break
                print("Posicoes livres na janela:")
                for i in range(7):
                    if janela_direita[i] == 0:
                        print((i + 1), end=" - ")
                polcompra = int(input("\nDigite o numero da poltrona desejada: "))
                janela_direita[polcompra - 1] = 'x'
                total_vendido = total_vendido + 1

            elif opcao2 == 'E':
                if janela_esquerda == ['x', 'x', 'x', 'x', 'x', 'x', 'x']:
                    print('Todos os lugares estão ocupados!')
                    break
                print("Posicoes livres na janela:")
                for i in range(7):
                    if janela_esquerda[i] == 0:
                        print((i + 1), end=" - ")
                polcompra = int(input("\nDigite o numero da poltrona desejada: "))
                janela_esquerda[polcompra - 1] = 'x'
                total_vendido = total_vendido + 1
            else:
                print('Opção inválida, tente novamente!')

        elif opcao == "C":
            opcao3 = str(input('Corredor direito [D] ou esquerdo [E]? ')).strip().upper()[0]
            if opcao3 == 'D':
                if corredor_direita == ['x', 'x', 'x', 'x', 'x', 'x', 'x']:
                    print('Todos os lugares estão ocupados!')
                    break
                for i in range(7):
                    if corredor_direita[i] == 0:
                        print((i + 1), end=" - ")
                polcompra = int(input("\nDigite o numero da poltrona desejada: "))
                corredor_direita[polcompra - 1] = 'x'
                total_vendido = total_vendido + 1

            elif opcao3 == 'E':
                if corredor_esquerda == ['x', 'x', 'x', 'x', 'x', 'x', 'x']:
                    print('Todos os lugares estão ocupados!')
                    break
                print("Posicoes livres no Corredor:")
                for i in range(7):
                    if corredor_esquerda[i] == 0:
                        print((i + 1), end=" - ")
                polcompra = int(input("\nDigite o numero da poltrona desejada: "))
                corredor_esquerda[polcompra - 1] = 'x'
                total_vendido = total_vendido + 1
            else:
                print('Opção inválida. Tente novamente!')

        else:
            print('Opção invalida')

        if total_vendido == 28:
            print()
            print('Todas as passagens foram vendidas')
            break

        comprar_2 = str(input('Deseja comprar outra passagem? [S/N]: ')).strip().upper()[0]
        if comprar_2 == 'S':
            limpar_tela()
            continue
        if comprar_2 == 'N':
            break

while True:
    menu_passagem()
    escolha = int(input('Digite sua opção: '))

    if escolha == 1:
        vender_passagem()

    if escolha == 2:
        poltronas()
        retornar = str(input('Deseja retornar ao Menu? [S/N]:')).strip().upper()[0]
        if retornar == 'S':
            print()
            continue
        else:
            print('    --- Obrigada por utlizar nossos serviços! ---')
            break

    if escolha == 3:
        with open('Relatorio_Pocco.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write(' Relatório de vendas das passagens POCCOBUS')
            arquivo.write(f'\n Foram vendidas {total_vendido} poltronas.')
            arquivo.write(f'\n Sobraram {28 - total_vendido} poltronas.')
        print('              RELATÓRIO GERADO   ')
        print('--- Obrigada por utlizar nossos serviços! ---')
        break

    if escolha == 4:
        print()
        print(f'Foram vendidas {total_vendido} poltronas')
        print()

        nova_venda = str(input('Deseja comprar mais passagens? [S/N]: ')).strip().upper()[0]
        if nova_venda == 'S':
            continue
        else:
            print('   --- Obrigada por utlizar nossos serviços! ---')
            break
    else:
        print('Opção inválida, tente novamente!')

input()