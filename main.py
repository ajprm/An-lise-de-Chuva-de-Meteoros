# Isso é um arquivo de projeto primário!! Primeiro projeto**
import math

sair = False
x1, y1, x3, y3, x1_edi, y1_edi, x3_edi, y3_edi = 0, 0, 0, 0, 0, 0, 0, 0  # as variáveis iniciam com 0 nas opções
meteoritos = []  # cria uma lista de meteoritos para depois analisar
perimetro_propriedade = 0  # o perímetro da propriedade inicia com 0 nas opções
perimetro_edificacao = 0  # o perímetro da edificação inicia com 0 nas opções
registros = 0  # o contador de registros de quedas de meteoritos inicia com 0 nas opções
quedas_dentro_propriedade = 0  # contador de quedas dentro da propriedade inicia com 0 nas opções
raio_edificacao = 0  # raio da fazenda/edificação inicia com 0 nas opções

while not sair:
    print("-:: Sistema para Análise de Chuva de Meteoros ::-")
    print("1. Definir perímetro da propriedade e da edificação de interesse")
    print("2. Unificar sistemas de coordenadas de referência")
    print('3. Processar registros de chuva de meteoros')
    print("4. Apresentar estatísticas")
    print('5. Sair')

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print("Sobre as coordenadas opostas da propriedade informe:")
        print()
        x1 = int(input("Digite a coordenada x da primeira extremidade: "))
        y1 = int(input("Digite a coordenada y da primeira extremidade: "))
        x3 = int(input("Digite a coordenada x da segunda extremidade: "))
        y3 = int(input("Digite a coordenada y da segunda extremidade: "))
        print()
        print("Agora sobre a edificação informe:")
        x1_edi = int(input("Digite a coordenada x da primeira extremidade: "))
        y1_edi = int(input("Digite a coordenada y da primeira extremidade: "))
        x3_edi = int(input("Digite a coordenada x da segunda extremidade: "))
        y3_edi = int(input("Digite a coordenada y da segunda extremidade: "))
        # Fazer o programa descobrir as outras coordenadas e o perímetro da propriedade
        x2 = x1
        y2 = y3
        x4 = x3
        y4 = y1
        coord1 = (x1, y1)
        coord2 = (x2, y2)
        coord3 = (x3, y3)
        coord4 = (x4, y4)
        lado1e3 = math.sqrt((x1 - x2) ** 2 + (y2 - y1) ** 2)
        lado2e4 = math.sqrt((x2 - x3) ** 2 + (y3 - y2) ** 2)
        perimetro_propriedade = 2 * (lado1e3 + lado2e4)
        # agora o da edificação
        x2_edi = x1_edi
        y2_edi = y3_edi
        x4_edi = x3_edi
        y4_edi = y1_edi
        # Fazer o programa descobrir as outras coordenadas e o perímetro da edificação
        coord1_edi = (x1_edi, y1_edi)
        coord2_edi = (x2_edi, y2_edi)
        coord3_edi = (x3_edi, y3_edi)
        coord4_edi = (x4_edi, y4_edi)
        lado1e3_edi = math.sqrt((x1_edi - x2_edi) ** 2 + (y2_edi - y1_edi) ** 2)
        lado2e4_edi = math.sqrt((x2_edi - x3_edi) ** 2 + (y3_edi - y2_edi) ** 2)
        perimetro_edificacao = 2 * (lado1e3_edi + lado2e4_edi)
        print()
        print("Perímetro da propriedade é: {}. E o perímetro da edificação é: {} ".format(perimetro_propriedade, perimetro_edificacao))
    elif escolha == "2":
        print("Você selecionou a Opção 2.")
        # Para descobrir a localização da fazenda e da sede, primeiro vou calcular o ponto médio de cada
        # PM_propriedade
        xm = (x1 + x3) / 2
        ym = (y1 + y3) / 2

        # PM_edificacao
        xm_edi = (x1_edi + x3_edi) / 2
        ym_edi = (y1_edi + y3_edi) / 2

        # Sobreposição de origem
        x_propriedade = xm - xm_edi
        y_propriedade = ym - ym_edi

        # Converta as coordenadas cartesianas da propriedade para coordenadas polares
        raio_propriedade = math.sqrt(x_propriedade ** 2 + y_propriedade ** 2)
        angulo_propriedade = math.atan2(y_propriedade, x_propriedade)

        print("Localização da propriedade em coordenadas polares: ({:.2f}, {:.2f} rad)".format(raio_propriedade, angulo_propriedade))

        # Agora, calcule as coordenadas cartesianas corrigidas em relação ao ponto de referência (0,0)
        x_propriedade_corrigido = x_propriedade - 0
        y_propriedade_corrigido = y_propriedade - 0

        print("Localização da propriedade em relação ao ponto de referência (0,0): ({:.2f}, {:.2f})".format(x_propriedade_corrigido, y_propriedade_corrigido))

    elif escolha == "3":
        print("Você selecionou a Opção 3.")

        # Aqui usa-se coordenadas polares
        num_meteoritos = int(input("Digite o número de meteoritos: "))

        contador_meteoritos = 0  # Inicialize o contador de meteoritos

        for i in range(num_meteoritos):
            x_meteorito = float(input("Digite a coordenada x do meteorito {}: ".format(i + 1)))
            y_meteorito = float(input("Digite a coordenada y do meteorito {}: ".format(i + 1)))

            # Calcula a localização do meteorito em relação à propriedade
            x_rel_propriedade = x_meteorito - x_propriedade
            y_rel_propriedade = y_meteorito - y_propriedade

            # Calcula a localização do meteorito em relação à edificação
            x_rel_edificacao = x_meteorito - x_edificacao
            y_rel_edificacao = y_meteorito - y_edificacao

            print("Localização do meteorito {} em relação à propriedade: ({:.2f}, {:.2f})".format(i + 1, x_rel_propriedade, y_rel_propriedade))
            print("Localização do meteorito {} em relação à edificação: ({:.2f}, {:.2f})".format(i + 1, x_rel_edificacao, y_rel_edificacao))

            # Verificar se o meteorito caiu dentro do perímetro da fazenda
            dentro_propriedade = 0 <= x_rel_propriedade <= perimetro_propriedade and 0 <= y_rel_propriedade <= perimetro_propriedade
            dentro_edificacao = 0 <= x_rel_edificacao <= perimetro_edificacao and 0 <= y_rel_edificacao <= perimetro_edificacao

            if dentro_propriedade:
                print("O meteorito {} caiu dentro do perímetro da fazenda.".format(i + 1))
            else:
                print("O meteorito {} não caiu dentro do perímetro da fazenda.".format(i + 1))

            if dentro_edificacao:
                print("O meteorito {} caiu dentro do perímetro da edificação.".format(i + 1))
            else:
                print("O meteorito {} não caiu dentro do perímetro da edificação.".format(i + 1))

            contador_meteoritos += 1  # Incrementa o contador de meteoritos

        print("Total de meteoritos dentro do perímetro da fazenda: {}".format(contador_meteoritos))

    elif escolha == "4":
        print("Você selecionou a Opção 4.")
        # Calculando o total das quedas
        total_quedas_registradas = registros
        percent_quedas_dentro_propriedade = (quedas_dentro_propriedade / total_quedas_registradas) * 100

        print(f"Total de quedas registradas: {total_quedas_registradas} ({percent_quedas_dentro_propriedade:.1f}%)")
        print(f"Quedas dentro da propriedade: {quedas_dentro_propriedade} ({percent_quedas_dentro_propriedade:.1f}%)")

        # Calcula a distribuição das quedas nos quadrantes
        quadrante_NE = 0
        quadrante_NO = 0
        quadrante_SO = 0
        quadrante_SE = 0

        for _ in range(quedas_dentro_propriedade):
            angulo = float(input("Digite o ângulo em relação ao eixo polar (direção leste) para uma queda dentro da propriedade: "))

            if 0 <= angulo < math.pi / 2:
                quadrante_NE += 1
            elif math.pi / 2 <= angulo < math.pi:
                quadrante_NO += 1
            elif math.pi <= angulo < 3 * math.pi / 2:
                quadrante_SO += 1
            else:
                quadrante_SE += 1

        print(f"-> Quadrante NE: {quadrante_NE} ({(quadrante_NE / quedas_dentro_propriedade) * 100:.2f}%)")
        print(f"-> Quadrante NO: {quadrante_NO} ({(quadrante_NO / quedas_dentro_propriedade) * 100:.2f}%)")
        print(f"-> Quadrante SO: {quadrante_SO} ({(quadrante_SO / quedas_dentro_propriedade) * 100:.2f}%)")
        print(f"-> Quadrante SE: {quadrante_SE} ({(quadrante_SE / quedas_dentro_propriedade) * 100:.2f}%)")

        # Verifica se a edificação principal foi atingida
        edificacao_atingida = False
        for _ in range(quedas_dentro_propriedade):
            angulo = float(input("Digite o ângulo em relação ao eixo polar (direção leste) para uma queda dentro da propriedade: "))

            distancia = raio_edificacao
            if 0 <= distancia <= perimetro_edificacao:
                edificacao_atingida = True
                break

        print("A edificação principal foi atingida? " + ("SIM" if edificacao_atingida else "NÃO"))

    elif escolha == "5":
        sair = True
#Participantes do grupo: Anna Julia Santos de Paula, DIOGO COSTA MACEDO e PEDRO GIOVANNINI ANDRADE