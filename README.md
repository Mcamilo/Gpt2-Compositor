# Gpt2-compositor
> Gerador de letras de músicas

Por meio do uso do [gpt-2 simple](https://github.com/minimaxir/gpt-2-simple) é possível o retreino do gerador de texto gpt-2 com uma bases de letras de músicas
coletadas com o [Vagalume-Letras-Crawler](https://github.com/Mcamilo/Vagalume-Letras-Crawler). 

Efetivamente permitindo a geração de letras de músicas com inteligência artificial.

## Instalação

OS X & Linux:

```sh
git clone https://github.com/Mcamilo/Gpt2-Compositor.git
cd /Gpt2-Compositor
pip3 install gpt-2-simple
```
## Caso de Uso

O repositório conta com um exemplo executado para o genêro "Bossa nova".

A lista completa de gêneros pode ser obtida [aqui](https://www.vagalume.com.br/browse/style/)

## Setup
A execução do arquivo finetune, faz o download do modelo pré-treinado e o refina para a aplicação em textos de letras de músicas. Esse modelo é salvo por default como /checkpoint/run1.
O main.py gera textos a partir do checkpoint criado.
```sh
python finetune.py
python main.py
```
## Meta

Desenvolvido durante o Hackathon [Code Stage](https://www.codestage.com.br/) Sony Music
Matheus Camilo – matheuscmilo@gmail.com

