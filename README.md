## Dati v2.0


### Iniciando

- Clone este  repository;
- Inicie o docker:
```
$ docker-compose up -d
```

- Acesse o repositório e ative o virtualenv:
```
$ source venv/bin/activate
```
ou
```
$ . venv/bin/activate

```
- Assumindo que você ja tenha o pip instalado,instale as bibliotecas:
```
$ python3 pip install -r requirements.txt
```

- Criando o banco:
```
$ python3 main.py
```
###### Pronto.
- Agora basta acessar <http://localhost:5002/clima/São Paulo> e ver os resultados.

