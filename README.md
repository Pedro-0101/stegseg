# stegseg

esconde mensagem dentro de imagem (esteganografia). grava os bits da mensagem no último bit do vermelho de cada pixel. simples assim.

precisa de python 3 e do pillow.

pip install Pillow

para esconder uma mensagem

py teste.py --operation hide --imagem imagem.png --mensagem "texto secreto" --output saida.png

para ler a mensagem em uma imagem

py teste.py --operation read --imagem saida.png

## argumentos

- --operation: hide ou read. se não passar nada, é hide
- --imagem: caminho da imagem. obrigatório
- --mensagem: o texto a esconder. se não passar, vai "Mensagem padrao"
- --output: onde salvar. se não passar, salva em saida.png

detalhes

- a gravação começa do meio da imagem e anda pixel por pixel
- se a imagem for pequena demais pra mensagem, o programa para sem salvar
- o `--operation read` só imprime a mensagem no terminal, ignora `--output`

como funciona

1. o texto vira bytes, cada byte vira 8 bits
2. cada bit entra no bit menos significativo do canal vermelho de um pixel
3. um byte zero no fim da mensagem marca o fim (é assim que a leitura sabe onde parar)
4. pra ler, percorre o mesmo caminho e junta os bits de volta
