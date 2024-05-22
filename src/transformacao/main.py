import pandas as pd
import numpy as np
import sqlite3
import datetime
import os

# COnfigurar o pandas para exibir todas
# as colunas do dataframe
pd.options.display.max_columns = None

arquivo = "./data/data.json"


# carregando o dataset
df = pd.read_json(arquivo)

# Criando colunas para site e data de coleta
df["source"] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"
df["data_coleta"] = datetime.datetime.now()


# Tratar os valores nulos para colunas numéricas e de texto
df["old_price_reais"] = df["old_price_reais"].fillna(0).astype(np.float32)
df["old_price_centavos"] = df["old_price_centavos"].fillna(0).astype(np.float32)
df["new_price_reais"] = df["new_price_reais"].fillna(0).astype(np.float32)
df["new_price_centavos"] = df["new_price_centavos"].fillna(0).astype(np.float32)
df["reviews_rating_number"] = df["reviews_rating_number"].fillna(0).astype(np.float32)


# Remover os parênteses das colunas `reviews_amount`
df["reviews_amount"] = df["reviews_amount"].str.replace("[\(\)]", "", regex=True)
df["reviews_amount"] = df["reviews_amount"].fillna(0).astype(int)

# Tratar os preços como floats e calcular os valores totais
df["old_price"] = df["old_price_reais"] + df["old_price_centavos"] / 100
df["new_price"] = df["new_price_reais"] + df["new_price_centavos"] / 100

# Remover as colunas antigas de preços
df.drop(columns=["old_price_reais", "old_price_centavos",
                 "new_price_reais", "new_price_centavos"], inplace=True)


# Conectar ao banco de dados SQLite (ou criar um novo)
conn = sqlite3.connect("./data/quotes.db")

# Salvar o DataFrame no banco de dados SQLite
df.to_sql("mercadolivre_items", conn, if_exists="replace", index=False)

# Fechar a conexão com o banco de dados
conn.close()

# Configurar pandas para mostrar todas as colunas
pd.options.display.max_columns = None

# Exibir o DataFrame resultante
print(df.head())
