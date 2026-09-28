import argparse
from PIL import Image


print("Pillow funcionando!")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Sistema de Esteganografia")
    parser.add_argument("--operation", type=str, help="Operação a ser executada: hide para esconder mensagem | read para ler uma mensagem")
    parser.add_argument("--imagem", type=str, help="Cole o caminho da imagem")
    parser.add_argument("--mensagem", type=str, help="Mensagem a ser escondida")
    parser.add_argument("--output", type=str, help="Local onde a mensagem ou imagem serão salvas")

    args = parser.parse_args()

    operation = args.operation
    imagem = args.imagem
    mensagem = args.mensagem
    output = args.output

    if operation == "":
        operation = "hide"

    if mensagem == "":
        mensagem = "Mensagem padrao"

    if output == "":
        output = "./"


    print(operation + " mensagem " + mensagem + " na imagem " + imagem + " e salvando o resultado em " + output)

    print(args)