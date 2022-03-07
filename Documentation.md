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