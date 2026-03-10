import numpy as np
import os
from PIL import Image

def codificar_RLE(sequencia: list) -> list:
    """
    Esta função procura por elementos iguais e acopla-os num conjunto
    (quantidade, valor)

    Args:
        sequencia (list): Lista de valores que serão codificados por RLE

    Returns:
        list: Retorna a sequencia codificada 
    """
    if not sequencia:
        return []
    
    codificado = []
    valor_atual = sequencia[0]
    count = 0
    
    for byte in sequencia:
        if byte == valor_atual and count < 255:
            count += 1
        else:
            codificado.append((count, valor_atual))
            valor_atual = byte
            count = 1
            
    codificado.append((count, valor_atual))
    return codificado

def descodificar_RLE(sequencia: list) -> list:
    """
    Esta função escreve numa nova lista a quantidade de valor dado 
    pelo count

    Args:
        sequencia (list): Lista codificada por RLE para ser descodificada.

    Returns:
        list: Retorna a sequencia descodificada
    """
    descodificado = []
    for count, pixel in sequencia:
        descodificado.extend([pixel] * count)
    return descodificado


def codificar_imagem(imagem:str) -> list|tuple:
    """
    A função converte a imagem para uma lista de tuplos de pixeis
    RGB (R, G, B) e criando tuplos (count, (R, G, B)) através da função
    codificar_RLE

    Args:
        imagem (str): O nome do ficheiro que o RLE irá comprimir

    Returns:
        list|tuple: Retorna três elementos: uma lista com os pixéis 
        codificados, o tamanho da imagem (tuplo[int, int]) e uma lista com
        os pixéis da imagem original
    """
    img = Image.open(imagem).convert('RGB')
    tamanho = img.size

    pixeis = list(img.getdata())

    codificado = codificar_RLE(pixeis)
    print(f"Primeiros 10 pixels: {list(pixeis[:10])}")
    print(f"Primeiros 10 pares codificados: {list(codificado[:10])}")
    
    return codificado, tamanho, pixeis



def descodificar_imagem(sequencia: list, tamanho:tuple) -> list:
    """
    Esta função cria uma nova imagem com o modo "RGB" e o tamanho do argumento
    e guarda como "imagem_restaurada.png", mostrando-a no fim.

    Args:
        sequencia (list): Sequencia que está codificada com RLE e será 
        descodificada
        tamanho (tuple): Tamanho da imagem original

    Returns:
        list: Retorna uma lista com os pixéis descodificados
    """
    decoded_pixels = descodificar_RLE(sequencia)

    new_img = Image.new('RGB', tamanho)
    new_img.putdata(decoded_pixels)
    new_img.save('imagem_restaurada.png')
    new_img.show()
    return decoded_pixels

def analise_tamanho(pixeis: list, codificado: list, descodificado: list) -> None:
    """
    Esta função analisa os tamanhos original, comprimido e descomprimido.
    Os pixéis nos tamanhos originais ocupam, cada, 3 bytes (R, G, B) enquanto
    os tuplos no codificado ocupam 4 bytes (valor, (R, G, B))

    Args:
        pixeis (list): lista de pixéis da imagem original
        codificado (list): lista de pixéis codificados
        descodificado (list): lista de pixéis descodificados
    """
    tamanho_original = len(pixeis) * 3
    tamanho_codificado = len(codificado) * 4
    tamanho_descodificado = len(descodificado) * 3
    diferenca = tamanho_original - tamanho_codificado
    fator_compressao = round(tamanho_original/tamanho_codificado, 2)

    print(f"Tamanho original: {tamanho_original} bytes") 
    print(f"Tamanho codificado: {tamanho_codificado} bytes")
    print(f"Diferença de bytes: {diferenca} bytes")
    print(f"Tamanho descodificado : {tamanho_descodificado} bytes")
    print(f"Fator de Compressão: {fator_compressao}")


def menu():
    imagem = ""
    lista = []
    print("Bem Vindo ao Compressor RLE")
    while True:
        print("1 - Correr RLE com uma pequena lista pré-feita")
        print("2 - Criar lista aleatória de elementos")
        print("3 - Comprimir lista de elementos com RLE")
        print("4 - Selecionar imagem")
        print("5 - Criar imagem aleatória")
        print("6 - Ver imagem")
        print("7 - Comprimir imagem usando RLE")
        print("8 - Sair")
        opcao = int(input("Escolha uma opção: "))
        match opcao:
            case 1:
                dados_teste = [10, 10, 10, 20, 20, 5, 255, 255]
                comprimido = codificar_RLE(dados_teste)
                descomprimido = descodificar_RLE(comprimido)

                print(f"Original: {dados_teste}")
                print(f"Comprimido: {list(comprimido)}")
                print(f"Sucesso: {dados_teste == list(descomprimido)}")
            
            case 2:
                lista = np.random.randint(0, 6, 100).tolist()

            case 3:
                comprimido = codificar_RLE(lista)
                descomprimido = descodificar_RLE(comprimido)
                print(f"Original: {lista}")
                print(f"Comprimido: {comprimido}")
                print(f"Sucesso: {lista == descomprimido}")

            case 4:
                nome = input("Seleciona uma imagem da pasta: ")
                diretorio = os.getcwd()
                for ficheiro in os.listdir(diretorio):
                    if nome == ficheiro:
                        imagem = nome
                        print(f"Imagem {imagem} encontrada!")

            case 5:
                print("1 - Grayscale")
                print("2 - RGB")
                opcao = int(input("Escolha a sua opção: "))
                match opcao:
                    case 1:
                        a = np.random.randint(0,255, (300, 300, 2), dtype=np.uint8)
                        img = Image.fromarray(a)
                        img.save("imagem_aleatoria_grayscale.png")
                    case 2:
                        a = np.random.randint(0,255, (300, 300, 3), dtype=np.uint8)
                        img = Image.fromarray(a)
                        img.save("imagem_aleatoria_rgb.png")
                    case _:
                        print("Opção inválida")
                    
            case 6:
                visualizar = Image.open(imagem)
                visualizar.show()

            case 7:
                imagem_codificada, tamanho_imagem, imagem_pixeis, \
                     = codificar_imagem(imagem)
                imagem_descodificada = descodificar_imagem(imagem_codificada,\
                                                             tamanho_imagem)
                analise_tamanho(imagem_pixeis, imagem_codificada, imagem_descodificada)
            case 8:
                print("Terminando o programa...")
                break
            
            case _:
                print("Opção Inválida")
    

menu()