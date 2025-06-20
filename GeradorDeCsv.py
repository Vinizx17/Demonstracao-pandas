import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Definir número de registros
num_registros = 1000

# Gerar colunas de exemplo
np.random.seed(42)  # Para reprodutibilidade

ids = np.arange(1, num_registros + 1)
produtos = np.random.choice(['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Impressora', 'Fone de Ouvido'], num_registros)
quantidades = np.random.randint(1, 10, size=num_registros)
precos_unitarios = np.round(np.random.uniform(50, 5000, size=num_registros), 2)
clientes = np.random.choice(['Cliente A', 'Cliente B', 'Cliente C', 'Cliente D', 'Cliente E'], num_registros)

# Gerar datas de venda entre 1º Jan 2024 e hoje
datas_venda = [
    (datetime(2024, 1, 1) + timedelta(days=random.randint(0, 365))).date()
    for _ in range(num_registros)
]

# Calcular valor total
valores_totais = quantidades * precos_unitarios

# Criar o DataFrame
df = pd.DataFrame({
    'id_venda': ids,
    'data_venda': datas_venda,
    'produto': produtos,
    'quantidade': quantidades,
    'preco_unitario': precos_unitarios,
    'valor_total': valores_totais,
    'cliente': clientes
})

# Salvar como CSV
df.to_csv('vendas.csv', index=False, sep=',')

print("Arquivo 'vendas.csv' gerado com sucesso!")
