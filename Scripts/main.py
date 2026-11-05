from pipelines import PokemonPipeline

#Instanciando a classe

pipeline = PokemonPipeline()

# Leitura e gravação dos dados em DataFrame

df_pokemon = pipeline.leitura_armazenamento_1a()

# Enviando dados do DataFrame para o banco de dados

pipeline.enviar_bd(df_pokemon)
