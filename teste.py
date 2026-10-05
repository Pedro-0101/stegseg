import argparse
from PIL import Image

def esconder_mensagem(imagem_add, mensagem, output):
    imagem = Image.open(imagem_add).convert("RGBA")
    pixels = imagem.load()

    tamanho = imagem.size
    posx = tamanho[0] // 2
    posy = tamanho[1] // 2

    mensagem_bin = ''.join(format(byte, '08b') for byte in bytearray(mensagem, 'utf-8') + b'\x00')
    print("Mensagem binaria: ", mensagem_bin)

    for m in mensagem_bin:
        r, g, b, a = pixels[posx, posy]
        r_alt = (r & ~1) | int(m)
        pixels[posx, posy] = (r_alt, g, b, a)

        posx += 1

        if posx == tamanho[0]:
            posx = 0

        if posx == tamanho[0] // 2 - 1:
            posy += 1

        if posy == tamanho[1]:
            posy = 0

        if posy == tamanho[1] // 2 - 1:
            exit(1)

    imagem.save(output)


def ler_mensagem(imagem_add):
    imagem = Image.open(imagem_add).convert("RGBA")
    pixels = imagem.load()

    tamanho = imagem.size
    posx = tamanho[0] // 2
    posy = tamanho[1] // 2

    mensagem_bin = ""
    mensagem = bytearray()

    while True:
        r, _, _, _ = pixels[posx, posy]
        mensagem_bin += str(r & 1)

        if len(mensagem_bin) == 8:
            byte = int(mensagem_bin, 2)

            if byte == 0:
                return mensagem.decode("utf-8")

            mensagem.append(byte)
            mensagem_bin = ""

        posx += 1

        if posx == tamanho[0]:
            posx = 0

        if posx == tamanho[0] // 2 - 1:
            posy += 1

        if posy == tamanho[1]:
            posy = 0

        if posy == tamanho[1] // 2 - 1:
            exit(1)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Sistema de Esteganografia")
    parser.add_argument("--operation", type=str, default="hide", help="Operação a ser executada: hide para esconder mensagem | read para ler uma mensagem")
    parser.add_argument("--imagem", type=str, required=True, help="Cole o caminho da imagem")
    parser.add_argument("--mensagem", type=str, default="Mensagem padrao", help="Mensagem a ser escondida")
    parser.add_argument("--output", type=str, default="saida.png", help="Local onde a mensagem ou imagem serão salvas")

    args = parser.parse_args()

    if args.operation == "hide":
        print("escondendo mensagem " + args.mensagem + " na imagem " + args.imagem + " e salvando o resultado em " + args.output)
        esconder_mensagem(args.imagem, args.mensagem, args.output)
    elif args.operation == "read":
        mensagem = ler_mensagem(args.imagem)
        print("Mensagem encontrada: " + mensagem)
    else:
        print("Operacao invalida: " + args.operation)
