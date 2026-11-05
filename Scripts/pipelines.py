import requests
import pandas as pd
import os
import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine, Integer, VARCHAR, Float
import time

class PokemonPipeline:

    def __init__(self):
        pass

    def leitura_armazenamento_1a(self):

        dados_poke = []

        for id in range(1, 151):

            url = f'https://pokeapi.co/api/v2/pokemon/{id}'

            try:
                response = requests.get(url, timeout=10)

                if response.status_code == 200:
                    dados = response.json()

                    dict_poke = {
                        'id': dados['id'],
                        'nome': dados['name'],
                        'altura': dados['height'],
                        'peso': dados['weight'],
                        'experiencia_concedida': dados['base_experience'],
                        'tipo_principal': dados['types'][0]['type']['name'],
                    }

                    dados_poke.append(dict_poke)

                    print(f"[{id}/150] {dados['name']} coletado!")

                else:
                    print(f"Erro {response.status_code} no ID {id}")

            except Exception as e:
                print(f"Falha de conexão no ID {id}: {e}")


            time.sleep(0.2)

        df_poke = pd.DataFrame(dados_poke)

        return df_poke


    def enviar_bd(self, df):

        load_dotenv()

        def get_conn():
            return psycopg2.connect(
                dbname=os.getenv("db_name"),
                user=os.getenv("db_user"),
                password=os.getenv("db_password"),
                host="localhost",
                port=os.getenv("db_port", "5432")
            )
        
        engine = create_engine("postgresql+psycopg2://", creator=get_conn)

        tabela_bd = 'pokemon_info'

        df.to_sql(tabela_bd, engine, index = False, if_exists='replace', dtype= {
                                            'id': Integer,
                                            'nome': VARCHAR(20),
                                            'altura': Float,
                                            'peso': Float,
                                            'experiencia_concedida': Integer,
                                            'tipo_principal': VARCHAR(25)}
                                            )     

        print(f'Dados gravados no banco com sucesso')

        engine.dispose()                                                               