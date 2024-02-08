# -*- coding: utf-8 -*-
import tweepy
import time



api = tweepy.Client(
    consumer_key = 'API KEY',
    consumer_secret = 'API Key Secret',
    access_token = 'Access Token',
    access_token_secret= 'access token secret'
)

with open('C:/Users/PC/Desktop/Projetos/AIstrologia/twitterzao.txt', 'r', encoding='utf-8') as file:
    texto_original = file.read()


mensagens = texto_original.split(".")

# Iterar sobre cada mensagem, remover espaços vazios e tweetar se não estiver vazio
for msg in mensagens:
    if msg:  # Verifica se a mensagem não está vazia
        try:
            tweet = api.create_tweet(text=msg)
            print(f"Tweet publicado: {tweet}")
            time.sleep(10)  # Espera 10 segundos antes de publicar o próximo tweet, pra não tomar um 429
        except Exception as e:
            print(f"Erro ao publicar tweet: {e}")
            print("Vai dormir")
