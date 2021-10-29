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






