import funcoes
from basededados import basenormal as base
from basededados import EARTH_RADIUS as raio
import time
import random
jogo = True
while jogo:
    # aqui é o códio principal, responsável por executar o jogo

    #   coisas importantes para o jogo

    with open('inventario_dicas.txt', 'w') as invd:
        invd.write('Dicas:\n\t')

    with open('inventario_paises.txt', 'w') as invp:
        invp.write('Distancias:\n\t')

    palpites = []
    cores = []
    cores_reveladas = []

    #   escolha de país
    paises = base.keys()
    pais = funcoes.sorteia_pais(base)
    capital = base[pais]["capital"]
    pop = base[pais]["populacao"]
    area = base[pais]["area"]
    continente = base[pais]["continente"]
    for c, n in base[pais]["bandeira"].items():
        if c!='outras' and n!=0:
            cores.append(c)
    lat = base[pais]["geo"]["latitude"]
    long = base[pais]["geo"]["longitude"]

    


    print('  ===========================\n||                          ||\n||       Insper Países      ||\n||                          ||\n  ===========================')

    #   Loop principal

    rodada = True
    tentativas = 20
    while rodada:
        with open('inventario_paises.txt', 'r') as inv:
            invpalpites = inv.read()
        with open('inventario_dicas.txt', 'r') as inv:
            invdicas = inv.read()
        print(f'{invpalpites}\n{invdicas}')
        print('Comandos:\n \tDica\t- Mostra as dica diponíveis.\n\tInventario\t- Mostra sua posição\n\tDesisto\t- desiste do jogo')
        print(f'Voce possui {tentativas} tentativas')

        comando = input('Digite um comando ou um palpite: ')

        if comando in paises:
            if comando not in palpites
                palpites.append(comando)

            lat1 = base[comando]["geo"]["latitude"]#    latitude do palpite
            long1 = base[comando]["geo"]["longitude"]#  longitude do palpite
            dist = funcoes.haversine(raio, lat, long, lat1, long1)
            with open('inventario_paises.txt', 'a') as invp:
                invp.write(f'{comando} - {dist} km\n\t')


        #         Caso acabe as tentativas
        if tentativas <= 0:
            rodada = False



        #       comando de dicas
        if comando.lower() == 'dica': 
            print('Mercado de Dicas \n ----------------------------------------\n\t1. Cor da bandeira  - custa 4 tentativas\n\t2. Letra da capital - custa 3 tentativas\n\t3. Área             - custa 6 tentativas\n\t4. População        - custa 5 tentativas\n\t5. Continente       - custa 7 tentativas\n\t0. Sem dica\n----------------------------------------')
            
            escolha = int(input('Escolha sua opção [0|1|2|3|4|5]: '))
            
            while escolha != 0 and escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5:
                    print('Opção inválida')
                    escolha = int(input('Escolha sua opção [0|1|2|3|4|5]: '))
            
            if escolha == 0:
                print('\n\tDistâncias:\n\tDicas:')

            if escolha == 1:    #cor da bandeira
                
                if tentativas-4 <= 0:
                    print('Você não possue tentativas o suficiente para comprar esta dica!')
                else:
                    cor = random.choice(cores)
                    cores_reveladas.append(cores)
                    cores.remove(cor)

                    with open('inventario_dicas.txt', 'a') as inv:
                        inv.write(f'Cores da bandeira: {cores_reveladas}')

                    tentativas -= 4
                    print('\n\tDistâncias:\n\tDicas:\n -Cores da bandeira: ')#adicionar ao lado da dica a cor da bandeira

            if escolha == 2:
                
                if tentativas -3 <= 0:
                    print('Você não possue tentativas o suficiente para comprar esta dica!')
                else:
                    tentativas -= 3
                    print('\n\tDistâncias:\n\tDicas:')#adicionar ao lado da dica a letra da capital

            if escolha == 3:
                
                if tentativas - 6 <=0:
                    print('Você não possue tentativas o suficiente para comprar esta dica!')
                else:
                    tentativas -= 6
                    print('\n\tDistâncias:\n\tDicas:')

            if escolha == 4:
                
                if tentativas - 5 <= 0:
                    print('Você não possue tentativas o suficiente para comprar esta dica!')
                else:
                    tentativas -= 5
                    print('\n\tDistâncias:\n\tDicas:')#adicionar ao lado da dica a população

            if escolha == 5:
                
                if tentativas -7 <= 0:
                    print('Você não possue tentativas o suficiente para comprar esta dica!')
                else:
                    tentativas -= 7
                    print('\n\tDistâncias:\n\tDicas:')#adicionar ao lado da dica o continente


    #           comando de desistência

        if comando.lower() == 'desisto': 
            desistindo = input('Tem certeza que deseja desistir da rodada? [s|n]')
            if desistindo == 'n':
                rodada = True
            if desistindo == 's':
                print(f'>>> Que deselegante desistir, o país era: {pais}')#adicinar o pais no float depois do era:
                rodada = False
            jogarnovamente = input('Jogar novamente? [s|n]' )
            if jogarnovamente == 's':
                rodada = False
            if jogarnovamente == 'n':
                time.sleep(1)
                print('\nObrigado por jogar!\n')
                time.sleep(1)
                print('\tAté a próxima!')
                jogo = False

    #               comando de inventario
        if comando.lower() == 'inventario':
            print('\n\tDistâncias:\n\tDicas:')#adicionar distancias e dicas

        