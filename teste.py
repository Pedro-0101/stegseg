import argparse
from PIL import Image

def esconder_mensagem(imagem_add, mensagem, output):
    imagem = Image.open(imagem_add).convert("RGBA")
    pixels = imagem.load()

    tamanho = imagem.size
    posx = tamanho[0]/2
    posy = tamanho[1]/2

    mensagem_bin = ' '.join(format(byte, '08b') for byte in bytearray(mensagem, 'utf-8'))
    print("Mensagem binaria: ", mensagem_bin)


    for m in range(list(mensagem_bin)):

        r, _, _, _ = pixels[posx, posy]
        r_bin = bin(r)

        r_lista = list(f"{r_bin}")
        r_lista[-1] = str(m)

        r_alt = int("".join(r_lista), 0)

        pixels[posx, posy]


        posx += 1

        if posx == tamanho[0]:
            posx = 0

        if posx == tamanho[0]/2 - 1:
            posy += 1

        if posy == tamanho[1]:
            posy = 0
        
        if posy == tamanho[1]/2 - 1:
            exit(1)

        pass

    # imagem.save(output)



if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Sistema de Esteganografia")
    parser.add_argument("--operation", type=str, help="Operação a ser executada: hide para esconder mensagem | read para ler uma mensagem")
    parser.add_argument("--imagem", type=str, help="Cole o caminho da imagem")
    parser.add_argument("--mensagem", type=str, help="Mensagem a ser escondida")
    parser.add_argument("--output", type=str, help="Local onde a mensagem ou imagem serão salvas")

    args = parser.parse_args()

    operation = args.operation
    imagem_add = args.imagem
    mensagem = args.mensagem
    output = args.output

    if operation == "":
        operation = "hide"

    if mensagem == "":
        mensagem = "Mensagem padrao"

    if output == "":
        output = "./"


    print(operation + " mensagem " + mensagem + " na imagem " + imagem_add + " e salvando o resultado em " + output)

    esconder_mensagem(imagem_add, mensagem, output)