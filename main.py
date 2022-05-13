import funcoes

# aqui é o códio principal, responsável por executar o jogo

print('  ===========================\n||                          ||\n||       Insper Países      ||\n||                          ||\n  ===========================')

# Loop principal
tentativas = 0#colocar limitador de 20 tentativas
jogo = True
tentativas = 20
while jogo:
    print('Comandos:\n \tDica\t- Mostra as dica diponíveis.\n\tInventario\t- Mostra sua posição\n\tDesisto\t- desiste do jogo')
    comando = input('Digite um comando ou um palpite: ')
    #         Caso acabe as tentativas
    if tentativas <= 0:
        jogo = False



    #       comando de dicas
    if comando.lower() == 'dica': 
        print('Mercado de Dicas \n ----------------------------------------\n\t1. Cor da bandeira  - custa 4 tentativas\n\t2. Letra da capital - custa 3 tentativas\n\t3. Área             - custa 6 tentativas\n\t4. População        - custa 5 tentativas\n\t5. Continente       - custa 7 tentativas\n\t0. Sem dica\n----------------------------------------')
        escolha = int(input('Escolha sua opção [0|1|2|3|4|5]: '))
        while escolha != 0 and escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5:
                print('Opção inválida')
                escolha = int(input('Escolha sua opção [0|1|2|3|4|5]: '))
        if escolha == 0:
            print('\n\tDistâncias:\n\tDicas:')

        if escolha == 1:
            tentativas -= 4
            if tentativas <= 3:
                print('Você não possue tentativas o suficiente para comprar esta dica!')
            else:
                print('\n\tDistâncias:\n\tDicas:')#adicionar ao lado da dica a cor da bandeira

        if escolha == 2:
            tentativas -= 3
            if tentativas <= 2:
                print('Você não possue tentativas o suficiente para comprar esta dica!')
            else:
                print('\n\tDistâncias:\n\tDicas:')#adicionar ao lado da dica a letra da capital

        if escolha == 3:
            tentativas -= 6
            if tentativas <= 5:
                print('Você não possue tentativas o suficiente para comprar esta dica!')
            else:
                print('\n\tDistâncias:\n\tDicas:')

        if escolha == 4:
            tentativas -= 5
            if tentativas <= 4:
                print('Você não possue tentativas o suficiente para comprar esta dica!')
            else:
                print('\n\tDistâncias:\n\tDicas:')#adicionar ao lado da dica a população

        if escolha == 5:
            tentativas -= 7
            if tentativas <= 6:
                print('Você não possue tentativas o suficiente para comprar esta dica!')
            else:
                print('\n\tDistâncias:\n\tDicas:')#adicionar ao lado da dica o continente


#           comando de desistência

    if comando.lower() == 'desisto': 
        desistindo = input('Tem certeza que deseja desistir da rodada? [s|n]')
        if desistindo == 'n':
            jogo = True
        if desistindo == 's':
            print(f'>>> Que deselegante desistir, o país era: ')#adicinar o pais no float depois do era:
            jogo = False
        jogarnovamente = input('Jogar novamente? [s|n]' )
        if jogarnovamente == 's':
            jogo = True
        if jogarnovamente == 'n':
            print('\n\n\tAté a próxima!')
            jogo = False

#               comando de inventario
    if comando.lower() == 'inventario':
        print('\n\tDistâncias:\n\tDicas:')#adicionar distancias e dicas

    