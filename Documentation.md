## Como rodar o app

### Requisitos(Tutorial funcional no ubuntu e em distros relacionadas)

-   Criar um ambiente virtual ```venv```, é preciso ter o venv instalado
    ```bash
        python3 -m venv venv
    ```

-   Ativar o ambiente virtual
    ```bash
        source venv/bin/activate
    ```

-   Instalar as libs que estão no ```requirements.txt```
    ```bash
        pip install -r requirements.txt 
    ```

### Rodando a aplicação

No diretório raiz, executar :

```bash
    python3 main.py
```


### endpoints

Os endpoints começam todos com ```/contact```

#### Cadastrar contato

    POST em /contact

```json
    {
        "name": "Teste Name",
        "phone_number" : "400289012"
    }
```

#### Retornar todos contatos

    GET em /contact/all

#### Update de numero

    PATCH /contact/update

```json
    {
        "old_phone_number": "123",
        "new_phone_number": "312"
    }
```

#### Delete de numero

    DELETE /contact/<phone_number>

    Para o numero "123456":
    A url fica /contact/123456




### Rodando os testes

```bash
    python3 -m pytest
```