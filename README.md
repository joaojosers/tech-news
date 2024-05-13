# tech-news

## Contexto
- Utilizar o terminal interativo do Python.
- Escrever seus próprios módulos e importá-los em outros códigos.
- Aplicar técnicas de raspagem de dados.
- Extrair dados de conteúdo HTML.
- Armazenar os dados obtidos em um banco de dados


## Tecnologias usadas
- Desenvolvido usando: Python e MongoDB
## Crie o ambiente virtual para o projeto
```
python3 -m venv .venv && source .venv/bin/activate
```
## Instalando Dependências
```
python3 -m pip install -r dev-requirements.txt
```
## Executando o projeto
- As notícias a serem raspadas estarão disponíveis no _Blog da Trybe_: https://blog.betrybe.com. 
- Essas notícias devem ser salvas no banco de dados utilizando as funções python que já vêm prontas no módulo `database.py`
MongoDB.
- Para a realização deste projeto, utilizaremos um banco de dados chamado tech_news.
- As notícias serão armazenadas em uma coleção chamada news. Já existem algumas funções prontas no arquivo tech_news/database.py.

* Rodar MongoDB via Docker:
```
docker compose up - d mongodb
```
## Executando Testes
* executando todos os testes
 ```
 python3 -m pytest
```
* Caso precise executar apenas um arquivo de testes basta executar o comando:
```
python3 -m pytest tests/nomedoarquivo.py
```
* Para fazer teste manual: Abra um terminal Python importando as funções de interesse através do comando:
```
python3 -i tech_news/arquivo_de_interesse.py
```
## Arquivos desenvolvidos pela Trybe
* src:
  - dev-requirements.txt
  - requirements.txt