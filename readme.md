# Projeto: Demonstração da biblioteca pandas com MinIO e Jupyter Notebook

Este projeto demonstra como utilizar o MinIO para armazenamento de arquivos (CSV) em conjunto com o Jupyter Notebook e a biblioteca Pandas para manipulação e análise de dados, tudo orquestrado por Docker Compose.

## Estrutura do Projeto

```
AIRFLOW/
├── dados/
│   └── vendas.csv
├── notebooks/
│   └── Demonstracao_pandas.ipynb
├── docker-compose.yml
└── gerador_csv
```

- `dados/`: Contém o arquivo exemplo `vendas.csv` utilizado nos notebooks.
- `notebooks/`: Notebooks Jupyter para demonstração prática das funções do Pandas.
- `docker-compose.yml`: Orquestra os serviços do MinIO e Jupyter Notebook.
- `gerador_csv`: Script ou ferramenta opcional para geração de dados.

## Como Executar

1. **Pré-requisitos**  
   - Docker e Docker Compose instalados.

2. **Subindo o ambiente**

   No diretório do projeto, execute:
   
   docker-compose up
   

3. **Acessando os serviços**

   - **Jupyter Notebook:**  
     Abra o navegador e acesse [http://localhost:8888](http://localhost:8888)  
     Utilize o token exibido no terminal do Jupyter para acesso.

   - **MinIO:**  
     Acesse [http://localhost:9000](http://localhost:9000)  
     Usuário e senha padrão:  
     - Usuário: `minioadmin`
     - Senha: `minioadmin`

## Exemplo de Uso

No notebook `notebooks/Demonstracao_pandas.ipynb`, você encontra exemplos de como:
- Ler arquivos CSV diretamente do MinIO usando Pandas
- Realizar operações de manipulação de dados


## Observações

- O script/ferramenta `gerador_csv` pode ser usado para criar arquivos de exemplo em `dados/`.
- Certifique-se de que as credenciais do MinIO e as configurações de endpoint estejam corretas.
- O Docker Compose facilita o provisionamento dos serviços necessários para o ambiente de análise de dados.

## Licença

Este projeto está licenciado sob a Licença Apache 2.0 — veja o arquivo [LICENSE](LICENSE) para detalhes.