# -*- coding: utf-8 -*-
import tweepy
import time
import os
import random

api = tweepy.Client(
    consumer_key = 'API KEY',
    consumer_secret = 'API Key Secret',
    access_token = 'Access Token',
    access_token_secret= 'access token secret'
)
# Caminho do diretório onde os arquivos .txt estão localizados
diretorio = 'C:/Users/PC/Desktop/Projetos/AIstrologia'

# Lista todos os arquivos no diretório que terminam com '.txt'
arquivos = [arq for arq in os.listdir(diretorio) if arq.endswith('.txt')]

# Escolhe um arquivo aleatoriamente dentre os arquivos .txt
arquivo_selecionado = random.choice(arquivos)

# Caminho completo do arquivo selecionado
caminho_completo = os.path.join(diretorio, arquivo_selecionado)

# Texto original que você quer tweetar, dividido por pontos

with open(caminho_completo, 'r', encoding='utf-8') as file:
    texto_original = file.read()


mensagens = texto_original.split(".")

# Iterar sobre cada mensagem, remover espaços vazios e tweetar se não estiver vazio
for msg in mensagens:
    if msg:  # Verifica se a mensagem não está vazia
        try:
            time.sleep(10)
            tweet = api.create_tweet(text=msg)
            print(f"Tweet publicado: {tweet}")
            time.sleep(10)  # Espera 10 segundos antes de publicar o próximo tweet
        except Exception as e:
            print(f"Erro ao publicar tweet: {e}")
            print("Vai dormir")
    time.sleep(10)