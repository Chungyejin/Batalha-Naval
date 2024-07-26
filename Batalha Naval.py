import random
import time

# menu do jogo
print("☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼ BATALHA NAVAL ☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼")
nome = input("\ninsira seu nome: ")
time.sleep(1)
print(
  f"\nbem-vindo a batalha naval, {nome}! \npara ganhar, você deve adivinhar as posições das embarcações do computador!"
)
time.sleep(3)
print("\npronto?")
time.sleep(1)
print("vamos jogar!\n")
time.sleep(1)

# tabuleiros fixos, tem as posições das embarcações!
mapacomputador = [
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ '],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ '],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ '],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ '],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ '],
]
mapajogador = [
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ '],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ '],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ '],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ '],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ '],
]
# tabuleiros que vão atualizando!
tabuleirocomputador = [
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ '],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ '],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ '],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ '],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ '],
]
tabuleirojogador = [
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ '],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ '],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ '],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ '],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ '],
]


def imprimetabuleiro(tabs):
  for linha in range(5):
    print("".join(tabs[linha]))


# coleta posicao porta-avião (ocupa 5 posições)
time.sleep(0.1)
print(f"\n\n----- tabuleiro {nome.casefold()} -----\n")
imprimetabuleiro(mapajogador)
print("------------------------------")
time.sleep(0.2)
linhapajogador = int(input("\nInsira o número da linha do porta-avião: "))
while linhapajogador < 1 or linhapajogador > 5:
  linhapajogador = int(input("Linha inválida! Escolha uma linha de 1 a 5: "))
colunapajogador = int(
  input("Insira o número da coluna de início do porta-avião (de 1 a 6): "))
while colunapajogador < 1 or colunapajogador > 6:
  colunapajogador = int(
    input("Coluna inválida! Escolha uma coluna de 1 a 6: "))
for i in range(5):
  mapajogador[linhapajogador - 1][colunapajogador - 1 + (1 * i)] = " x "

# coleta posicao navio-tanque (ocupando 4 posições)
time.sleep(0.1)
print(f"\n\n----- tabuleiro {nome.casefold()} -----\n")
imprimetabuleiro(mapajogador)
print("------------------------------")
time.sleep(0.2)
linhantjogador = int(input("\nInsira o número da linha do navio-tanque: "))
while linhantjogador < 1 or linhantjogador > 5:
  linhantjogador = int(input("Linha inválida! Escolha uma linha de 1 a 5: "))
colunantjogador = int(
  input("Insira o número da coluna de início do navio-tanque (de 1 a 7): "))
while colunantjogador < 1 or colunantjogador > 7:
  colunantjogador = int(
    input("Coluna inválida! Escolha uma coluna de 1 a 6: "))
for i in range(4):
  mapajogador[linhantjogador - 1][colunantjogador - 1 + (1 * i)] = " x "

# coleta posicao contratorpedeiro (ocupando 3 posições)
time.sleep(0.1)
print(f"\n\n----- tabuleiro {nome.casefold()} -----\n")
imprimetabuleiro(mapajogador)
print("------------------------------")
time.sleep(0.2)
linhactjogador = int(input("\nInsira o número da linha do contratorpedeiro: "))
while linhactjogador < 1 or linhactjogador > 5:
  linhactjogador = int(input("Linha inválida! Escolha uma linha de 1 a 5: "))
colunactjogador = int(
  input(
    "Insira o número da coluna de início do contratorpedeiro (de 1 a 8): "))
while colunactjogador < 1 or colunactjogador > 8:
  colunactjogador = int(
    input("Coluna inválida! Escolha uma coluna de 1 a 8: "))
for i in range(3):
  mapajogador[linhactjogador - 1][colunactjogador - 1 + (1 * i)] = " x "

# coleta posicao submarino (ocupando 2 posições)
time.sleep(0.1)
print(f"\n\n----- tabuleiro {nome.casefold()} -----\n")
imprimetabuleiro(mapajogador)
print("------------------------------")
time.sleep(0.2)
linhasubjogador = int(input("\nInsira o número da linha do submarino: "))
while linhasubjogador < 1 or linhasubjogador > 5:
  linhasubjogador = int(input("Linha inválida! Escolha uma linha de 1 a 5: "))
colunasubjogador = int(
  input("Insira o número da coluna de início do submarino (de 1 a 9): "))
while colunasubjogador < 1 or colunasubjogador > 9:
  colunasubjogador = int(
    input("Coluna inválida! Escolha uma coluna de 1 a 9: "))
for i in range(2):
  mapajogador[linhasubjogador - 1][colunasubjogador - 1 + (1 * i)] = " x "

# coleta posicao destroier (ocupando 1 posição)
time.sleep(0.1)
print(f"\n\n----- tabuleiro {nome.casefold()} -----\n")
imprimetabuleiro(mapajogador)
print("------------------------------")
time.sleep(0.2)
linhadjogador = int(input("\nInsira o número da linha do destroier: "))
while linhadjogador < 1 or linhadjogador > 5:
  linhadjogador = int(input("Linha inválida! Escolha uma linha de 1 a 5: "))
colunadjogador = int(input("Insira o número da coluna do destroier: "))
while colunadjogador < 1 or colunadjogador > 10:
  colunadjogador = int(
    input("Coluna inválida! Escolha uma coluna de 1 a 10: "))
mapajogador[linhadjogador - 1][colunadjogador - 1] = " x "

print(f"\n\n----- tabuleiro {nome.casefold()} -----\n")
imprimetabuleiro(mapajogador)
print("------------------------------")

# gera randomicamente as posições das embarcações do computador
# porta-avião (ocupa 5 posições)
linhapacomputador = random.randint(0, 4)
colunapacomputador = random.randint(0, 5)
for i in range(5):
  mapacomputador[linhapacomputador][colunapacomputador + (1 * i)] = " x "

# navio-tanque (4 posições)
linhantcomputador = random.randint(0, 4)
colunantcomputador = random.randint(0, 6)
# evita posições repetidas
while mapacomputador[linhantcomputador][colunantcomputador] != ' ≈ ' and mapacomputador[linhantcomputador][
    colunantcomputador + 1] != ' ≈ ' and mapacomputador[linhantcomputador][colunantcomputador + 2] != ' ≈ ' and \
        mapacomputador[linhantcomputador][colunantcomputador + 3] != ' ≈ ':
  linhantcomputador = random.randint(0, 4)
  colunantcomputador = random.randint(0, 6)
for i in range(4):
  mapacomputador[linhantcomputador][colunantcomputador + (1 * i)] = " x "

# contratorpedeiro (3 posições)
linhactcomputador = random.randint(0, 4)
colunactcomputador = random.randint(0, 7)
# evita posições repetidas
while mapacomputador[linhactcomputador][
    colunactcomputador] != ' ≈ ' and mapacomputador[linhactcomputador][
      colunactcomputador + 1] != ' ≈ ' and mapacomputador[linhactcomputador][
        colunactcomputador + 2] != ' ≈ ':
  linhactcomputador = random.randint(0, 4)
  colunactcomputador = random.randint(0, 7)
for i in range(3):
  mapacomputador[linhactcomputador][colunactcomputador + (1 * i)] = " x "

# submarino (2 posições)
linhasubcomputador = random.randint(0, 4)
colunasubcomputador = random.randint(0, 8)
# evita posições repetidas
while mapacomputador[linhasubcomputador][
    colunasubcomputador] != ' ≈ ' and mapacomputador[linhasubcomputador][
      colunasubcomputador + 1] != ' ≈ ':
  linhasubcomputador = random.randint(0, 4)
  colunasubcomputador = random.randint(0, 8)
for i in range(2):
  mapacomputador[linhasubcomputador][colunasubcomputador + (1 * i)] = " x "

# destroier (1 posição)
linhadcomputador = random.randint(0, 4)
colunadcomputador = random.randint(0, 9)
# evita posições repetidas
while mapacomputador[linhadcomputador][colunadcomputador] != ' ≈ ':
  linhadcomputador = random.randint(0, 4)
  colunadcomputador = random.randint(0, 9)
mapacomputador[linhadcomputador][colunadcomputador] = " x "


def checajogada(mapa, tabuleiro, linha, coluna):
  if mapa[linha][coluna] == " x ":
    tabuleiro[linha][coluna] = " x "
    time.sleep(1)
    print("\n⚑ parabéns! acertou\n")
    return 1

  else:
    tabuleiro[linha][coluna] = " o "
    time.sleep(1)
    print("\n⚐ triste... errou\n")
    return 0


def imprimetabuleiros():
  # imprime tabuleiro do computador
  time.sleep(2)
  print("\n---- tabuleiro computador ----\n")
  for linha in range(5):
    print("".join(tabuleirocomputador[linha]))
  print("------------------------------")
  print(f"embarcações restantes: {embarcacoescomputador()}")

  #  imprime tabuleiro do jogador
  time.sleep(1)
  print(f"\n\n----- tabuleiro {nome.casefold()} -----\n")
  for linha in range(5):
    print("".join(tabuleirojogador[linha]))
  print("------------------------------")
  print(f"embarcações restantes: {embarcacoesjogador()}")
  time.sleep(3)


def jogadajogador(embarcacoesinimigas):
  imprimetabuleiros()
  if embarcacoesinimigas == 0:
    return 0

  # recebe a jogada do jogador
  linhajogador = int(input("\n\n\ninsira a linha que deseja atacar: "))
  colunajogador = int(input("insira a coluna que deseja atacar: "))
  linhajogador -= 1
  colunajogador -= 1

  # evita jogadas inválidas
  while linhajogador < 0 or linhajogador > 4 or colunajogador < 0 or colunajogador > 9:
    print(
      "\n\nposição inválida... insira uma linha (um valor de 1 a 5) e coluna (um valor de 1 a 10)!"
    )
    linhajogador = int(input("\ninsira a linha que deseja atacar: "))
    colunajogador = int(input("insira a coluna que deseja atacar: "))
    linhajogador -= 1
    colunajogador -= 1

  # evita jogadas repetidas
  while tabuleirocomputador[linhajogador][colunajogador] != ' ≈ ':
    print("\n\nposição já jogada... insira uma nova!")
    linhajogador = int(input("\ninsira a linha que deseja atacar: "))
    colunajogador = int(input("insira a coluna que deseja atacar: "))
    linhajogador -= 1
    colunajogador -= 1

  # checa jogada do jogador
  if checajogada(mapacomputador, tabuleirocomputador, linhajogador,
                 colunajogador) == 1:
    return 1  # joga de novo!!!!
  else:
    return 2  # vez do computador


def jogadacomputador(embarcacoesinimigas):
  imprimetabuleiros()
  if embarcacoesinimigas == 0:
    return 0

  # recebe a jogada do computador
  linhacomputador = random.randint(0, 4)
  colunacomputador = random.randint(0, 9)

  # evitar jogadas repetidas
  while tabuleirojogador[linhacomputador][colunacomputador] != ' ≈ ':
    linhacomputador = random.randint(0, 4)
    colunacomputador = random.randint(0, 9)

  print(f"\n\n\ncomputador escolheu linha {linhacomputador + 1}")
  time.sleep(3)  # suspense
  print(f"computador escolheu coluna {colunacomputador + 1}")

  # checa jogada do computador
  if checajogada(mapajogador, tabuleirojogador, linhacomputador,
                 colunacomputador) == 1:
    return 1  # joga de novo
  else:
    return 3  # vez do jogador


def checaportaaviao(mapa, tabuleiro, linha, coluna):
  for i in range(5):
    if tabuleiro[linha][coluna + (1 * i)] != mapa[linha][coluna + (1 * i)]:
      return 1  # diz que ainda há uma embarcação caso não estejam todas preenchidas
  return 0


def checanaviotanque(mapa, tabuleiro, linha, coluna):
  for i in range(4):
    if tabuleiro[linha][coluna + (1 * i)] != mapa[linha][coluna + (1 * i)]:
      return 1  # diz que ainda há uma embarcação caso não estejam todas preenchidas
  return 0


def checacontratorpedeiro(mapa, tabuleiro, linha, coluna):
  for i in range(3):
    if tabuleiro[linha][coluna + (1 * i)] != mapa[linha][coluna + (1 * i)]:
      return 1  # diz que ainda há uma embarcação caso não estejam todas preenchidas
  return 0


def checasubmarino(mapa, tabuleiro, linha, coluna):
  for i in range(2):
    if tabuleiro[linha][coluna + (1 * i)] != mapa[linha][coluna + (1 * i)]:
      return 1  # diz que ainda há uma embarcação caso não estejam todas preenchidas
  return 0


def checadestroier(mapa, tabuleiro, linha, coluna):
  if tabuleiro[linha][coluna] != mapa[linha][coluna]:
    return 1
  return 0


def embarcacoescomputador():
  return checaportaaviao(
    mapacomputador, tabuleirocomputador,
    linhapacomputador, colunapacomputador) + checanaviotanque(
      mapacomputador, tabuleirocomputador,
      linhantcomputador, colunantcomputador) + checacontratorpedeiro(
        mapacomputador, tabuleirocomputador,
        linhactcomputador, colunactcomputador) + checasubmarino(
          mapacomputador, tabuleirocomputador,
          linhasubcomputador, colunasubcomputador) + checadestroier(
            mapacomputador, tabuleirocomputador, linhadcomputador,
            colunadcomputador)


def embarcacoesjogador():
  return checaportaaviao(mapajogador, tabuleirojogador, linhapajogador - 1,
                         colunapajogador - 1) + checanaviotanque(
                           mapajogador, tabuleirojogador, linhantjogador - 1,
                           colunantjogador - 1) + checacontratorpedeiro(
                             mapajogador, tabuleirojogador, linhactjogador - 1,
                             colunactjogador - 1) + checasubmarino(
                               mapajogador, tabuleirojogador, linhasubjogador -
                               1, colunasubjogador - 1) + checadestroier(
                                 mapajogador, tabuleirojogador,
                                 linhadjogador - 1, colunadjogador - 1)


def mensagensjogador(pa, cn, ct, sub, d):
  if checaportaaviao(mapacomputador, tabuleirocomputador, linhapacomputador,
                     colunapacomputador) == 0 and pa == 0:
    time.sleep(1)
    print("⚑ afundou o porta-avião!\n")
    return 1
  if checanaviotanque(mapacomputador, tabuleirocomputador, linhantcomputador,
                      colunantcomputador) == 0 and cn == 0:
    time.sleep(1)
    print("⚑ afundou o navio-tanque!\n")
    return 2
  if checacontratorpedeiro(mapacomputador, tabuleirocomputador,
                           linhactcomputador,
                           colunactcomputador) == 0 and ct == 0:
    time.sleep(1)
    print("⚑ afundou o contratorpedeiro!\n")
    return 3
  if checasubmarino(mapacomputador, tabuleirocomputador, linhasubcomputador,
                    colunasubcomputador) == 0 and sub == 0:
    time.sleep(1)
    print("⚑ afundou o submarino!\n")
    return 4
  if checadestroier(mapacomputador, tabuleirocomputador, linhadcomputador,
                    colunadcomputador) == 0 and d == 0:
    time.sleep(1)
    print("⚑ afundou o destroier!\n")
    return 5


def mensagenscomputador(pa, cn, ct, sub, d):
  if checaportaaviao(mapajogador, tabuleirojogador, linhapajogador - 1,
                     colunapajogador - 1) == 0 and pa == 0:
    time.sleep(1)
    print("⚑ afundou o porta-avião!\n")
    return 1
  if checanaviotanque(mapajogador, tabuleirojogador, linhantjogador - 1,
                      colunantjogador - 1) == 0 and cn == 0:
    time.sleep(1)
    print("⚑ afundou o navio-tanque!\n")
    return 2
  if checacontratorpedeiro(mapajogador, tabuleirojogador, linhactjogador - 1,
                           colunactjogador - 1) == 0 and ct == 0:
    time.sleep(1)
    print("⚑ afundou o contratorpedeiro!\n")
    return 3
  if checasubmarino(mapajogador, tabuleirojogador, linhasubjogador - 1,
                    colunasubjogador - 1) == 0 and sub == 0:
    time.sleep(1)
    print("⚑ afundou o submarino!\n")
    return 4
  if checadestroier(mapajogador, tabuleirojogador, linhadjogador - 1,
                    colunadjogador - 1) == 0 and d == 0:
    time.sleep(1)
    print("⚑ afundou o destroier!\n")
    return 5


# COMEÇA O JOGO
print("\n\n\n☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼ INICIANDO O JOGO ☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼")

# definir variáveis para imprimir mensagens de "afundou" uma única vez
pac = 0
cnc = 0
ctc = 0
subc = 0
dc = 0
paj = 0
cnj = 0
ctj = 0
subj = 0
dj = 0

# o jogo acontece enquanto ainda restar embarcações!
while embarcacoescomputador() != 0 and embarcacoesjogador() != 0:

  # VEZ DO JOGADOR
  jogada = jogadajogador(embarcacoescomputador())
  if jogada == 0:
    break  # caso o jogador tenha ganhado
  # joga novamente se acertar!
  while jogada == 1:
    mensagens = mensagensjogador(paj, cnj, ctj, subj, dj)
    if mensagens == 1:
      paj = 1
    if mensagens == 2:
      cnj = 1
    if mensagens == 3:
      ctj = 1
    if mensagens == 4:
      subj = 1
    if mensagens == 5:
      dj = 1

    jogada = jogadajogador(embarcacoescomputador())
  if jogada == 0:
    break

  # VEZ DO COMPUTADOR
  jogada = jogadacomputador(embarcacoesjogador())
  if jogada == 0:
    break
  # joga de novo se acertar!
  while jogada == 1:

    mensagens = mensagenscomputador(pac, cnc, ctc, subc, dc)
    if mensagens == 1:
      pac = 1
    if mensagens == 2:
      cnc = 1
    if mensagens == 3:
      ctc = 1
    if mensagens == 4:
      subc = 1
    if mensagens == 5:
      dc = 1

    jogada = jogadacomputador(embarcacoesjogador())

  if jogada == 0:
    break

# verifica o vencedor
if embarcacoescomputador() == 0:
  vencedor = nome
if embarcacoesjogador() == 0:
  vencedor = "COMPUTADOR"

# mensagem final
print("\n\n≋≋≋≋≋≋≋≋≋≋≋≋≋≋ FIM DE JOGO ≋≋≋≋≋≋≋≋≋≋≋≋≋≋")
time.sleep(1)
print(f"\n             ♆ {vencedor.upper()} VENCEU ♆")
time.sleep(1)
print(f"\n\nobrigada por jogar, {nome.capitalize()}!")
print("\njogo desenvolvido por: Anna, Andressa, Letícia, Michele e Yejin")
