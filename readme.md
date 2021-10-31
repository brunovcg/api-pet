# Iniciando um projeto DJANGO

## Linguagens necessárias:
- Tenha o Python instalado na sua máquina

##  Instalando
Após baixar esta aplicação usando o GIT CLONE:

1 - Inicie um ambiente virtual com o comando no terminal:

$ python -m venv venv

2 - Inicialize o ambiente virtual

$ source venv/bin/activate

3 - Instale as dependências do projeto com o comando:

$ pip install -r requirements.txt

(esse comando inicializará o django e o djangorestframework)

4 - Faça as migrations do banco:

$ python manage.py makemigrations

5 - Commit as migrations:

$ ./manage.py makemigrations

6 - Inicialize o servidor:

$ python manage.py runserver


# Rotas

## Animals

### POST api/animals/ - Cadastrando um Animal

#### Exemplo de Request:
```json
{
    "name": "Bidu",
    "age": 1,
    "weight": 30,
    "sex": "macho",
    "group": {
      "name": "cao",
      "scientific_name": "canis familiaris"
    },
    "characteristics": [
      {
        "name": "peludo"
      },
      {
        "name": "medio porte"
      }
    ]
  }
```
#### Response - HTTP 201 CREATED

```json
  {
    "id": 1,
    "name": "Bidu",
    "age": 1.0,
    "weight": 30.0,
    "sex": "macho",
    "group": {
      "id": 1,
      "name": "cao",
      "scientific_name": "canis familiaris"
    },
    "characteristics": [
      {
        "id": 1,
        "name": "peludo"
      },
      {
        "id": 2,
        "name": "medio porte"
      }
    ]
  }
    
```

### GET api/animals/ - Fazendo a leitura de todos os animais cadastrados:

#### Exemplo de Request:

Não contem Body

#### Response HTTP 200 OK

```json

[
    {
      "id": 1,
      "name": "Bidu",
      "age": 1,
      "weight": 30,
      "sex": "macho",
      "group": {
        "id": 1,
        "name": "cao",
        "scientific_name": "canis familiaris"
      },
      "characteristics": [
        {
          "id": 1,
          "name": "peludo"
        },
        {
          "id": 2,
          "name": "medio porte"
        }
      ]
    },
    {
      "id": 2,
      "name": "Hanna",
      "age": 1,
      "weight": 20,
      "sex": "femea",
      "group": {
        "id": 2,
        "name": "gato",
        "scientific_name": "felis catus"
      },
      "characteristics": [
        {
          "id": 1,
          "name": "peludo"
        },
        {
          "id": 3,
          "name": "felino"
        }
      ]
    }
  ]

```

### GET api/animals/<int:animal_id>/ - Filtrando animais:

Passa-se o id do animal como param


#### Exemplo de Request:
ex: api/animals/1/

Não contem Body

#### Response HTTP 200 OK

```json

  {
    "id": 1,
    "name": "Bidu",
    "age": 1,
    "weight": 30,
    "sex": "macho",
    "group": {
      "id": 1,
      "name": "cao",
      "scientific_name": "canis familiaris"
    },
    "characteristics": [
      {
        "id": 1,
        "name": "peludo"
      },
      {
        "id": 2,
        "name": "medio porte"
      }
    ]
  }

```

### Response HTTP 404 NOT_FOUND

Quando o ID não é encontrado


### DELETE api/animals/<int:animal_id>/ - deletando animais:

Passa-se como param o ID do animal a ser deletado



#### Exemplo de Request:
ex: api/animals/1/

Não há body

### Response HTTP 204 HTTP_204_NO_CONTENT


### Response HTTP 404 NOT_FOUND

Caso o ID não exista






