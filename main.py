import funcoes

# aqui é o códio principal, responsável por executar o jogo

print('  ===========================\n||                          ||\n||       Insper Países      ||\n||                          ||\n  ===========================')

# Loop principal
tentativas = 0#colocar limitador de 20 tentativas
jogo = True
while jogo:
    print('comandos:\n \tdica\t- Mostra as dica diponíveis.\n\tinventário\t- Mostra sua posição\n\tDesisto\tdesiste do jogo')
    comando = input('Digite um comando ou um palpite: ')
    #dicas



    if comando.lower() == 'desisto':
        jogo = False
    if comando.lower() == 'dica': 
        print('Mercado de Dicas \n ----------------------------------------\n\t1. Cor da bandeira  - custa 4 tentativas\n\t2. Letra da capital - custa 3 tentativas\n\t3. Área             - custa 6 tentativas\n\t4. População        - custa 5 tentativas\n\t5. Continente       - custa 7 tentativas\n\t0. Sem dica\n----------------------------------------')
        escolha = int(input('Escolha sua opção [0|1|2|3|4|5]: '))
        while escolha != 0 or escolha != 1 or escolha != 2 or escolha != 3 or escolha != 4 or escolha != 5:
            print('Opção inválida')
            escolha = int(input('Escolha sua opção [0|1|2|3|4|5]: '))
        if escolha == 0:
            print('\n\tDistâncias:\n\tDicas:')
            jogo = True
        if escolha == 1:
            tentativas += 4
            print('\n\tDistâncias:\n\tDicas:')#adicionar ao lado da dica a cor da bandeira
            jogo = True
        if escolha == 2:
            tentativas += 3
            print('\n\tDistâncias:\n\tDicas:')#adicionar ao lado da dica a letra da capital
            jogo = True
        if escolha == 3:
            tentativas += 6
            print('\n\tDistâncias:\n\tDicas:')
            jogo = True
        if escolha == 4:
            tentativas += 5
            print('\n\tDistâncias:\n\tDicas:')#adicionar ao lado da dica a população
            jogo = True
        if escolha == 5:
            tentativas += 7
            print('\n\tDistâncias:\n\tDicas:')#adicionar ao lado da dica o continente
            jogo = True