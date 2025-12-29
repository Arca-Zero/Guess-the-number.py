#---------------------------------------------------------------------------------------------------------------------------------------------
# DESAFIO: JOGO DE PALPITE # VERSÃO 1
import random # <----- ESSENCIAL; Sempre no topo. Permite utilizar certos comandos da biblioteca de 'aleatórios' do Python

numero_escolhido = random.randint(1, 1000) # Escolhe um número aleatório entre 1 e 1000.
palpitador = 0 # Variável onde se é armazenado o valor do input do jogador
tentativas = 0 # Variável do número de tentativas até acertar o numero_escolhido
while True: # Faz um Loop 'infinito'
    palpitador = int(input('Escolha o número\n')) # A variável Palpitador é igual ao número escolhido pelo 'jogador'[a pessoa que tá digitando o número]
    tentativas += 1 # Adiciona +1 na variável de tentativas sempre que o código se repete. Ou seja, até que o Loop acabe, ou seja, Break, adicione semrpe +1 na Variável tentativas
    distancia = abs(palpitador - numero_escolhido) # Variavel distância é igual a subtração do número que o jogador escolheu e do número escolhido aleatoriamente pela máquina. O abs() antes do parametro serve para, ao invés de dar um número negativo, retornar um número positivo.
    if distancia == 0: # Caso a variavel seja igual a 0, ou seja, caso a subtração dos números do jogador e da máquina resulte em 0, acaba o Loop, o que resulta numa vitória.
        print(f'🔥 PARABÉNS! Você acertou na mosca!')
        print(f'Aqui estão suas tentativas: {tentativas}') # Mostra o número total de tentativas antes que o Loop terminasse, ou seja, antes que o jogador acertasse o número da máquina.
        break 
    elif distancia <= 2: # Assim como nos outros Elif's, o código 'distância <= ?' significa basicamente: 'se distância for menor que ?'. Caso distancia seja menor que 2, mostra essa dica no terminal e continua o loop. Caso seja igual a zero, quebre o Loop. (Como visto lá em cima)
        print("SANGUE DE JESUS! Tá colado, você sentiu o cheiro do número!")
        continue # Continue aqui e nos outros elif's são totalmente desnecessários, mas como eu coloquei por colocar, vou deixar ai.
    elif distancia <= 5:
        print("Meu Deus! Tá super perto!")
        continue
    elif distancia <= 10:
        print("Muito perto! Se fosse uma cobra te picava.")
        continue
    elif distancia <= 30:
        print("Tá quente! Tá chegando na vizinhança.")
        continue
    elif distancia <= 80:
        print("Morno... você não está totalmente perdido.")
        continue
    elif distancia <= 150:
        print("Frio. Tá precisando de um GPS.")
        continue
    elif distancia <= 300:
        print("Gelado! Tá lá no Alasca, longe demais.")
        continue
    else:
        print("Tá super longe, amigão")
        continue
#---------------------------------------------------------------------------------------------------------------------------------------------
