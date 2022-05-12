import funcoes

# aqui é o códio principal, responsável por executar o jogo

print('  ===========================\n||                          ||\n||       Insper Países      ||\n||                          ||\n  ===========================')

# Loop principal

jogo = True
while jogo:
    print('comandos:\n \tdica\t- Mostra as dica diponíveis.\n\tinventário\t- Mostra sua posição\n\tDesisto\tdesiste do jogo')
    comando = input('Digite um comando ou um palpite')
    #dicas



    if comando.lower() == 'desisto':
        jogo = False