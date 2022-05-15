import funcoes
from basededados import basenormal as base
from basededados import EARTH_RADIUS as raio
import time
import random
jogo = True
while jogo:
    # aqui é o códio principal, responsável por executar o jogo
    #   numero total de tentativas

    tentativas = 20
    qnts_tentativas = 0
    # para o merdaco de dicas
    
    #   coisas importantes para o jogo

    with open('inventario_dicas.txt', 'w') as invd:
        invd.write('Dicas:\n\t')

    with open('inventario_paises.txt', 'w') as invp:
        invp.write('Distancias:\n\t')

    palpites = []
    distancias = []
    cores = []
    indice3 = 0
    indice4 = 0
    indice5 = 0
    dicas_usadas = {

    }

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
    
    while rodada:
        with open('inventario_paises.txt', 'w') as inv:
            inv.write('Distancias:\n\t')
        with open('inventario_paises.txt', 'a') as inv:
            for d in distancias:
                inv.write(f'{d[0]} - {d[1]:.2f} km\n\t')
        with open('inventario_paises.txt', 'r') as inv:
            invpaises = inv.read()

        with open('inventario_dicas.txt', 'w') as inv:
            inv.write('Dicas: \n\t')
        with open('inventario_dicas.txt', 'a') as inv:
            for k, v in dicas_usadas.items():
                inv.write(f'{k}: {v}\n\t')
        with open('inventario_dicas.txt', 'r') as inv:
            invdicas = inv.read()

        print(f'{invpaises}\n{invdicas}')
        print('Comandos:\n\tDica\t- Mostra as dica diponíveis.\n\tInventario\t- Mostra sua posição\n\tDesisto\t- desiste do jogo')
        print(f'Voce possui {tentativas} tentativas!')

        #   Para o mercado de dicas
        d1 = '1|' if tentativas-4>0 else ''
        d2 = '2|' if tentativas-3>0 else ''
        d3 = '3|' if tentativas-6>0 else ''
        d4 = '4|' if tentativas-5>0 else ''
        d5 = '5|' if tentativas-7>0 else ''

        D1 = '1. Cor da bandeira  - custa 4 tentativas' if tentativas-4>0 else ''
        D2 = '2. Letra da capital - custa 3 tentativas' if tentativas-3>0 else ''
        D3 = '3. Área             - custa 6 tentativas' if tentativas-6>0 else ''
        D4 = '4. População        - custa 5 tentativas' if tentativas-5>0 else ''
        D5 = '5. Continente       - custa 7 tentativas' if tentativas-7>0 else ''






        comando = input('Digite um comando ou um palpite: ')

        if comando in paises:

            if comando not in paises and comando.lower() != 'dica' and comando.lower() == 'inventario' and comando.lower() != 'desito':
                print('comando ou país inválido.')
       
            if comando not in palpites:
                tentativas -= 1
                qnts_tentativas += 1
                lat1 = base[comando]["geo"]["latitude"]#    latitude do palpite
                long1 = base[comando]["geo"]["longitude"]#  longitude do palpite
                dist = funcoes.haversine(raio, lat, long, lat1, long1)
                palpites.append(comando)
                distancias = funcoes.adiciona_em_ordem(comando, dist, distancias)

                with open('inventario_paises.txt', 'a') as invp:
                    invp.write(f'{comando} - {dist} km\n\t')

        # Caso o jogador ganhe
        if comando == pais:
            print(f'*** Parabéns! ***\n\tVocê acertou após {qnts_tentativas} tentativas!')
            jogardenovo = input('Jogar novamente? [s|n]' )
            if jogardenovo != 's' and jogardenovo != 'n':
                print('responda com s ou n')
                jogardenovo = input('Jogar novamente? [s|n]' )
            if jogardenovo == 's':
                rodada = False
            if jogardenovo == 'n':
                print('\nO cara é brabo!\n')
                time.sleep(1)
                print('\nObrigado por jogar!\n')
                rodada = False
                jogo = False






        #         Caso acabe as tentativas
        if tentativas == 0:
            print(f'>>> Você perdeu, o país era: {pais}')
            jogardenovo = input('Jogar novamente? [s|n]' )
            if jogardenovo != 's' and jogardenovo != 'n':
                print('responda com s ou n')
                jogardenovo = input('Jogar novamente? [s|n]' )
            if jogardenovo == 's':
                rodada = False
            if jogardenovo == 'n':
                rodada = False
                jogo = False





        #       comando de dicas
        if comando.lower() == 'dica': 
            print(f'Mercado de Dicas \n ----------------------------------------\n\t{D1}\n\t{D2}\n\t{D3}\n\t{D4}\n\t{D5}\n\t0. Sem dica\n----------------------------------------')
            
            escolha = int(input(f'Escolha sua opção [0|{d1}{d2}{d3}{d4}{d5}]: '))
            
            while escolha != 0 and escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5:
                    print('Opção inválida')
                    escolha = int(input(f'Escolha sua opção [0|{d1}{d2}{d3}{d4}{d5}]: '))
            






            if escolha == 1:    #cor da bandeira
                if len(cores) == 0:
                    time.sleep(0.5)
                    print('\n\nNão há mais cores diferentes!\n')
                    time.sleep(1)


                if len(cores) > 0:
                    if tentativas-4 <= 0:
                        time.sleep(1)
                        print('\n\nVocê não possue tentativas o suficiente para comprar esta dica!\n')
                        time.sleep(1)                   
                    else:
                        if 'Cores da bandeira' not in dicas_usadas:
                            dicas_usadas['Cores da bandeira'] = ''
                        cor = random.choice(cores)
                        dicas_usadas['Cores da bandeira']+=f'{cor}.' if dicas_usadas['Cores da bandeira'] == '' else f', {cor}.'
                        cores.remove(cor)

                        tentativas -= 4
                        qnts_tentativas += 4









            if escolha == 2:    # letra da capital
                
                if tentativas -3 <= 0:
                    time.sleep(1)
                    print('\n\nVocê não possue tentativas o suficiente para comprar esta dica!\n')
                    time.sleep(1)
                else:
                    if 'Letra da capital' not in dicas_usadas:
                        indice = 0
                        dicas_usadas['Letra da capital'] = capital[indice]
                        tentativas -= 3
                        qnts_tentativas += 3
                    else:
                        indice+=1 
                        if indice<len(capital):
                            dicas_usadas['Letra da capital'] +=capital[indice]
                            tentativas -= 3
                            qnts_tentativas += 3

                    if indice >= len(capital):
                        time.sleep(1)
                        print('\nO nome da capital ja está completo!\n')
                        time.sleep(1)


            if escolha == 3:    # area
                
                if tentativas - 6 <=0:
                    time.sleep(1)
                    print('\n\nVocê não possue tentativas o suficiente para comprar esta dica!\n')
                    time.sleep(1)
                else:
                    if indice3 == 0:
                        tentativas -= 6
                        qnts_tentativas += 6
                        dicas_usadas['area'] = area
                    if indice3 > 0:
                        time.sleep(1)
                        print('\nA área ja foi revelada!\n')
                        time.sleep(1)
                    indice3 += 1
                    

            if escolha == 4:    # populacao
                
                if tentativas - 5 <= 0:
                    time.sleep(1)
                    print('\n\nVocê não possue tentativas o suficiente para comprar esta dica!\n')
                    time.sleep(1)
                else:
                    if indice4 == 0:
                        tentativas -= 5
                        qnts_tentativas += 5
                        dicas_usadas['populacao'] = pop
                    if indice4 > 0:
                        time.sleep(1)
                        print('\nA população ja foi revelada!\n')
                        time.sleep(1)
                    indice4 += 1

            if escolha == 5:    # continente
                
                if tentativas -7 <= 0:
                    time.sleep(1)
                    print('\n\nVocê não possue tentativas o suficiente para comprar esta dica!\n')
                    time.sleep(1)
                else:
                    if indice5 == 0:
                        tentativas -= 7
                        qnts_tentativas += 7
                        dicas_usadas['continente'] = continente
                    if indice5 > 0:
                        time.sleep(1)
                        print('\nO continente ja foi revelado!\n')
                        time.sleep(1)
                    indice5 += 1

    #           comando de desistência

        if comando.lower() == 'desisto': 
            desistindo = input('Tem certeza que deseja desistir da rodada? [s|n]')            
            if desistindo == 's':
                print(f'>>> Que deselegante desistir, o país era: {pais}')#adicinar o pais no float depois do era:

                jogarnovamente = input('Jogar novamente? [s|n]' )
                if jogarnovamente == 's':

                    print('\nGerando a próxima rodada...\n')
                    time.sleep(1)
                    rodada = False
                if jogarnovamente == 'n':
                    time.sleep(1)
                    print('\nObrigado por jogar!\n')
                    time.sleep(1)
                    print('\tAté a próxima!')
                    rodada = False
                    jogo = False

    #               comando de inventario
        if comando.lower() == 'inventario':
            print(f'\n\t{invdicas}\n\t{invpaises}')#adicionar distancias e dicas

        