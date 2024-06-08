# ASCII Art Generator

Este script converte imagens em arte ASCII, mantendo a proporção e melhorando o contraste e os detalhes através da pixelização da imagem.

## Requisitos

- Python 3.x
- Pillow (biblioteca Python para manipulação de imagens)

## Instalação

1. Clone este repositório ou baixe o script.
2. Instale a biblioteca Pillow, se ainda não estiver instalada:
    ```sh
    pip install Pillow
    ```

## Uso

1. Execute o script `ascii_art.py`:
    ```sh
    python ascii_art.py
    ```

2. Quando solicitado, insira o caminho completo para a imagem que você deseja converter.

3. O script processará a imagem e exibirá a arte ASCII no console.

4. A arte ASCII gerada será salva em um arquivo chamado `ascii_image.txt` no mesmo diretório do script.

## Parâmetros Ajustáveis

- **Largura Base**: A largura da arte ASCII pode ser ajustada mudando o valor da variável `base_width` no script. O valor padrão é 100.
- **Tamanho de Pixelização**: O nível de pixelização poderá ser ajustado em futuro commit. O valor padrão é 10.

## Exemplo de Uso

```sh
python ascii_art.py
Enter a valid pathname to an image:
path/to/your/image.jpg
```
## Notas
A lista de caracteres ASCII usados para a arte vai do mais escuro até o mais claro, o que ajuda a melhorar o contraste e a representação de sombras.
A pixelização pode ser aplicada para simplificar a imagem e acentuar os detalhes, ajudando na conversão para arte ASCII.
## Contribuição
Sinta-se à vontade para fazer fork deste repositório e enviar pull requests com melhorias ou correções.
## Licença
Este projeto está licenciado sob a MIT License.
## Estrutura do Repositório
```shell
ascii-art-generator/
│
├── ascii_art.py
└── README.md
```
