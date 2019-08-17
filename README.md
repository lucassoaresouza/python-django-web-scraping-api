# Web Scraping com Python Django

## Introdução

Este sistema tem como objetivo principal a realização de uma coleta de dados de produtos presentes na página encontrada no seguinte link:

* https://nerdstore.com.br/categoria/especiais/game-of-thrones/  

Os dados são extraídos utilizando a técnica *web scraping* e são disponibilizados em um arquivo json.

## Instalação:

### 1 - Docker e Docker-Compose

Para executar o sistema é necessário possuir o **docker** e o **docker-compose** instalados em seu ambiente. Você pode verificar como instalar estas ferramentas nos links a seguir:

* [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [docker-compose](https://docs.docker.com/compose/install/)

### 2 - Executando

Tendo o docker e o docker-compose instalados em seu ambiente execute os passos a seguir:

```

$ docker-compose -f docker-compose.yml build

```

A imagem docker será então construída. Execute o comando a seguir para rodar o sistema:

```

$ docker-compose -f docker-compose.yml up

```

Em outra janela do terminal execute o seguinte comando para rodar as **migrations** do banco de dados:

```

$ docker-compose run web python3 manage.py migrate

```

Após as **migrations** serem executadas o sistema está pronto para uso!

## Json com os Dados:

Assim serão executados os containers referentes à API e seu banco de dados. Após o retorno positivo deste segundo comando é possível acessar os dados coletados no seguinte link:

* http://localhost:8000/products/?format=json

## Novo Scraping

Como também é realizado um novo Scraping todas as vezes em que o seguinte link é acessado:

* http://localhost:8000/scraping/
